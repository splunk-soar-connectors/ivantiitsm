# File: ivantiitsm_connector.py
#
# Copyright (c) 2017-2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Phantom App imports
import base64
import json
import math
from datetime import datetime, timedelta
from urllib.error import HTTPError

import phantom.app as phantom
import phantom.rules as ph_rules
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector
from suds.client import Client
from suds.plugin import DocumentPlugin, MessagePlugin
from suds.sudsobject import asdict
from suds.transport.http import HttpAuthenticated

import ivantiitsm_consts as consts
from ivantiitsm_xml_validation import LimitedXmlResponse, reject_unsafe_xml_declarations


MAX_XML_RESPONSE_BYTES = 16 * 1024 * 1024
SENSITIVE_RESPONSE_FIELDS = frozenset({"internalauthpasswd", "tempinternalauthpassword"})


class _LimitedHttpTransport(HttpAuthenticated):
    def u2open(self, request):
        try:
            return LimitedXmlResponse(super().u2open(request), MAX_XML_RESPONSE_BYTES)
        except HTTPError as error:
            error.fp = LimitedXmlResponse(error.fp, MAX_XML_RESPONSE_BYTES)
            raise


class _RejectUnsafeXmlPlugin(DocumentPlugin, MessagePlugin):
    @staticmethod
    def _validate(payload):
        content = payload.encode("utf-8") if isinstance(payload, str) else bytes(payload)
        if len(content) > MAX_XML_RESPONSE_BYTES:
            raise ValueError("Ivanti ITSM XML response exceeds the 16 MiB safety limit")
        reject_unsafe_xml_declarations(payload)

    def loaded(self, context):
        self._validate(context.document)

    def received(self, context):
        self._validate(context.reply)


class RetVal(tuple):
    def __new__(cls, val1, val2):
        return tuple.__new__(RetVal, (val1, val2))


class HeatConnector(BaseConnector):
    def __init__(self):
        # Call the BaseConnectors init first
        super().__init__()

        self._state = None
        self._proxy = None
        self._client = None
        self._base_url = None
        self._username = None
        self._password = None
        self._session_key = None

    def initialize(self):
        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        # get the asset config
        config = self.get_config()

        # Access values in asset config by the name
        self._username = config["username"]
        self._password = config["password"]
        self._base_url = config["url"] + ("" if config["url"].endswith("/") else "/")
        self._tenant = self._base_url.replace("/", "").replace("https:", "")

        self._proxy = {}
        env_vars = config.get("_reserved_environment_variables", {})
        if "HTTP_PROXY" in env_vars:
            self._proxy["http"] = env_vars["HTTP_PROXY"]["value"]
        if "HTTPS_PROXY" in env_vars:
            self._proxy["https"] = env_vars["HTTPS_PROXY"]["value"]

        return phantom.APP_SUCCESS

    def finalize(self):
        # Save the state, this data is saved accross actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS

    def _connect(self, action_result):
        try:
            client_options = {
                "plugins": [_RejectUnsafeXmlPlugin()],
                "transport": _LimitedHttpTransport(),
            }
            if self._proxy:
                client_options["proxy"] = self._proxy
            self._client = Client(
                url="{}{}".format(self._base_url, "ServiceAPI/FRSHEATIntegration.asmx?wsdl"),
                **client_options,
            )

            ret_val, response = self._make_soap_call(action_result, "Connect", (self._username, self._password, self._tenant, "Admin"))
            if not ret_val:
                return ret_val

            self._session_key = response["sessionKey"]

        except Exception as e:
            return action_result.set_status(phantom.APP_ERROR, "Could not connect to the ITSM API endpoint", e)

        return phantom.APP_SUCCESS

    def _make_soap_call(self, action_result, method, soap_args=()):
        if not hasattr(self._client.service, method):
            return RetVal(action_result.set_status(phantom.APP_ERROR, f"Could not find given method {method}"), None)

        soap_call = getattr(self._client.service, method)

        try:
            response = soap_call(*soap_args)
        except Exception as e:
            return RetVal(action_result.set_status(phantom.APP_ERROR, "SOAP call to ITSM failed", e), None)

        return True, self._strip_sensitive_fields(self._suds_to_dict(response))

    def _strip_sensitive_fields(self, value):
        if isinstance(value, dict):
            return {key: self._strip_sensitive_fields(child) for key, child in value.items() if key.casefold() not in SENSITIVE_RESPONSE_FIELDS}
        if isinstance(value, list):
            return [self._strip_sensitive_fields(child) for child in value]
        return value

    def _suds_to_dict(self, sud_obj):
        if hasattr(sud_obj, "__keylist__"):
            sud_dict = asdict(sud_obj)
            new_dict = {}

            if sud_dict.get("WebServiceFieldValue"):
                for inner_sud_obj in sud_dict["WebServiceFieldValue"]:
                    mini_dict = asdict(inner_sud_obj)
                    value = mini_dict.get("Value")
                    if isinstance(value, datetime):
                        value = value.strftime(consts.HEAT_TIME_FORMAT)
                    new_dict[mini_dict["Name"]] = value
                return new_dict

            for key in sud_dict:
                new_dict[key] = self._suds_to_dict(sud_dict[key])

            return new_dict

        elif isinstance(sud_obj, list):
            new_list = []
            for elm in sud_obj:
                new_list.append(self._suds_to_dict(elm))
            return new_list

        elif isinstance(sud_obj, datetime):
            return sud_obj.strftime(consts.HEAT_TIME_FORMAT)

        # Checking for NaN
        try:
            if math.isnan(float(sud_obj)):
                return None
        except Exception:
            self.debug_print(f"{sud_obj} is not a numeric value")

        return sud_obj

    def _add_attachment(self, action_result, ticket_id, vault_id):
        self.save_progress("Adding attachment to ticket")

        # Check for file in vault
        try:
            success, _, files_array = ph_rules.vault_info(vault_id=vault_id)
            if not success:
                return action_result.set_status(phantom.APP_ERROR, f"Attach failed: {consts.HEAT_ERROR_FILE_NOT_IN_VAULT}")
        except:
            return action_result.set_status(phantom.APP_ERROR, f"Attach failed: {consts.HEAT_ERROR_FILE_NOT_IN_VAULT}")

        files_array = next(iter(files_array))

        # Attach file to ticket
        try:
            path = files_array["path"]
            with open(path, "rb") as f:
                f64 = base64.b64encode(f.read())
        except Exception as e:
            return action_result.set_status(phantom.APP_ERROR, f"Attach failed: Could not read vault file: {e!s}")

        command_obj = self._client.factory.create("ObjectAttachmentCommandData")
        command_obj.ObjectType = "Incident#"
        command_obj.fileName = files_array["name"]
        command_obj.ObjectId = ticket_id
        command_obj.fileData = f64.decode("utf-8")

        ret_val, response = self._make_soap_call(
            action_result,
            "AddAttachment",
            (
                self._session_key,
                self._tenant,
                command_obj,
            ),
        )

        if phantom.is_fail(ret_val):
            return ret_val

        return phantom.APP_SUCCESS

    def _handle_test_connectivity(self, param):
        # Add an action result object to self (BaseConnector) to represent the action for this param
        self.debug_print("Running test connectivity")
        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        # Return success
        self.save_progress("Test Connectivity Passed")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_on_poll(self, param):
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        config = self.get_config()

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        poll_end_time = datetime.utcnow().strftime(consts.HEAT_TIME_FORMAT)
        update_checkpoint = not self.is_poll_now()
        if self.is_poll_now():
            start_time = (datetime.utcnow() - timedelta(days=int(config["poll_now_ingestion_span"]))).strftime(consts.HEAT_TIME_FORMAT)
        elif self._state.get("first_run", True):
            start_time = (datetime.utcnow() - timedelta(days=int(config["first_scheduled_ingestion_span"]))).strftime(consts.HEAT_TIME_FORMAT)
        else:
            checkpoint = datetime.strptime(self._state["last_time"], consts.HEAT_TIME_FORMAT) - timedelta(seconds=1)
            start_time = checkpoint.strftime(consts.HEAT_TIME_FORMAT)

        from_date_obj = self._client.factory.create("RuleClass")
        from_date_obj._Condition = ">"
        from_date_obj._Join = "AND"
        from_date_obj._Field = "CreatedDateTime"
        from_date_obj._Value = start_time

        rule_arr = self._client.factory.create("ArrayOfRuleClass")
        rule_arr.Rule = [from_date_obj]

        select_obj = self._client.factory.create("SelectClass")
        select_obj._All = True

        from_obj = self._client.factory.create("FromClass")
        from_obj._Object = "Incident"

        query_obj = self._client.factory.create("ObjectQueryDefinition")
        query_obj.From = from_obj
        query_obj.Where = rule_arr
        query_obj.Select = select_obj

        ret_val, response = self._make_soap_call(
            action_result,
            "Search",
            (
                self._session_key,
                self._tenant,
                query_obj,
            ),
        )

        if phantom.is_fail(ret_val):
            return ret_val

        tickets = response.get("objList", {}).get("ArrayOfWebServiceBusinessObject", {})
        if not tickets:
            if update_checkpoint:
                self._state["first_run"] = False
                self._state["last_time"] = poll_end_time
            return action_result.set_status(phantom.APP_SUCCESS, "No tickets to ingest")

        failed_tickets = 0
        for ticket in tickets:
            ticket = ticket.get("WebServiceBusinessObject", [{}])[0]

            if not ticket:
                failed_tickets += 1
                continue

            ticket_id = ticket.get("RecID")
            ticket = ticket.get("FieldValues", {})
            if not ticket_id or not ticket.get("Subject") or not ticket.get("Symptom"):
                failed_tickets += 1
                continue

            container = {}
            container["name"] = ticket["Subject"]
            container["description"] = ticket["Symptom"]
            container["source_data_identifier"] = ticket_id

            ret_val, message, container_id = self.save_container(container)

            if phantom.is_fail(ret_val):
                failed_tickets += 1
                self.debug_print(f"Could not save Ivanti ticket {ticket_id}: {message}")
                continue

            artifact = {}
            artifact["label"] = "ticket"
            artifact["name"] = "Ticket Fields"
            artifact["container_id"] = container_id
            artifact["source_data_identifier"] = ticket_id

            cef = {}
            for k, v in ticket.items():
                if v is not None:
                    cef[k] = v
            artifact["cef"] = cef
            artifact["cef_types"] = {
                "Email": ["email"],
                "OwnershipAssignmentEmail": ["email"],
                "OwnerTeamEmail": ["email"],
                "ServiceOwnerEmail": ["email"],
                "TeamManagerEmail": ["email"],
                "RecId": ["heat ticket id"],
            }

            self.save_artifact(artifact)

        if failed_tickets:
            return action_result.set_status(
                phantom.APP_ERROR,
                f"Failed to ingest {failed_tickets} Ivanti ticket(s); the polling checkpoint was not advanced",
            )

        if update_checkpoint:
            self._state["first_run"] = False
            self._state["last_time"] = poll_end_time
        self.debug_print("on poll action succeeded.")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_run_query(self, param):
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")
        self.debug_print(param)

        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        query_dict = param.get("query_dict")
        from_date = param.get("from_date")
        to_date = param.get("to_date")

        if not (query_dict or from_date or to_date):
            return action_result.set_status(phantom.APP_ERROR, "Must include one of query_dict, from_date, or to_date parameters")

        rules = []

        if from_date:
            from_date_obj = self._client.factory.create("RuleClass")
            from_date_obj._Condition = ">"
            from_date_obj._Join = "AND"
            from_date_obj._Field = "CreatedDateTime"
            from_date_obj._Value = from_date  # datetime.strptime(from_date, consts.HEAT_TIME_FORMAT)
            rules.append(from_date_obj)

        if to_date:
            to_date_obj = self._client.factory.create("RuleClass")
            to_date_obj._Condition = "<"
            to_date_obj._Join = "AND"
            to_date_obj._Field = "CreatedDateTime"
            to_date_obj._Value = to_date
            rules.append(to_date_obj)

        if query_dict:
            try:
                query_dict = json.loads(query_dict)
            except Exception as e:
                return action_result.set_status(phantom.APP_ERROR, f"Could not parse JSON from query_dict parameter: {e}")

            if not isinstance(query_dict, dict):
                return action_result.set_status(phantom.APP_ERROR, "Could not parse JSON from query_dict parameter")

            for k, v in query_dict.items():
                rule_obj = self._client.factory.create("RuleClass")
                rule_obj._Condition = "="
                rule_obj._Join = "AND"
                rule_obj._Field = k
                rule_obj._Value = v

                rules.append(rule_obj)

        rule_arr = self._client.factory.create("ArrayOfRuleClass")
        rule_arr.Rule = rules

        select_obj = self._client.factory.create("SelectClass")
        select_obj._All = True

        from_obj = self._client.factory.create("FromClass")
        from_obj._Object = "Incident"

        query_obj = self._client.factory.create("ObjectQueryDefinition")
        query_obj.From = from_obj
        query_obj.Where = rule_arr
        query_obj.Select = select_obj

        # make soap call
        ret_val, response = self._make_soap_call(
            action_result,
            "Search",
            (
                self._session_key,
                self._tenant,
                query_obj,
            ),
        )

        if phantom.is_fail(ret_val):
            return ret_val

        if response:
            action_result.add_data(response)

        num_tickets = len(response.get("objList", {}).get("ArrayOfWebServiceBusinessObject", []))
        summary = action_result.update_summary({})
        summary["num_tickets"] = num_tickets

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_create_ticket(self, param):
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")
        self.debug_print(param)

        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        subject = param["summary"]
        symptom = param["description"]
        service = param["service"]
        category = param["category"]
        customer = param["customer"]
        fields = param.get("fields")
        attachment = param.get("attachment")

        subject_obj = self._client.factory.create("ObjectCommandDataFieldValue")
        subject_obj.Name = "Subject"
        subject_obj.Value = subject

        symptom_obj = self._client.factory.create("ObjectCommandDataFieldValue")
        symptom_obj.Name = "Symptom"
        symptom_obj.Value = symptom

        service_obj = self._client.factory.create("ObjectCommandDataFieldValue")
        service_obj.Name = "Service"
        service_obj.Value = service

        category_obj = self._client.factory.create("ObjectCommandDataFieldValue")
        category_obj.Name = "Category"
        category_obj.Value = category

        customer_obj = self._client.factory.create("ObjectCommandDataFieldValue")
        customer_obj.Name = "ProfileLink"
        customer_obj.Value = customer

        field_objs = [subject_obj, symptom_obj, service_obj, category_obj, customer_obj]

        if fields:
            try:
                fields_dict = json.loads(fields)
            except Exception as e:
                return action_result.set_status(phantom.APP_ERROR, f"Could not parse JSON from query_dict parameter: {e}")

            if not isinstance(fields_dict, dict):
                return action_result.set_status(phantom.APP_ERROR, "Could not parse JSON from query_dict parameter")

            for field, value in fields_dict.items():
                field_obj = self._client.factory.create("ObjectCommandDataFieldValue")
                field_obj.Name = field
                field_obj.Value = value
                field_objs.append(field_obj)

        field_arr_obj = self._client.factory.create("ArrayOfObjectCommandDataFieldValue")
        field_arr_obj.ObjectCommandDataFieldValue = field_objs

        command_obj = self._client.factory.create("ObjectCommandData")
        command_obj.ObjectType = "Incident#"
        command_obj.Fields = field_arr_obj

        ret_val, response = self._make_soap_call(
            action_result,
            "CreateObject",
            (
                self._session_key,
                self._tenant,
                command_obj,
            ),
        )

        if phantom.is_fail(ret_val):
            return ret_val

        if response.get("status") == "Error":
            return action_result.set_status(phantom.APP_ERROR, "Could not create the ticket: {}".format(response.get("exceptionReason")))

        ticket_id = response["recId"]
        action_result.add_data(response)
        action_result.set_summary({"created_ticket_id": ticket_id})

        if attachment:
            attach_result = self._add_attachment(action_result, ticket_id, attachment)
            if not attach_result:
                return attach_result

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_ticket(self, param):
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")
        self.debug_print(param)

        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        ticket_id = param["id"]
        fields = param.get("fields")
        attachment = param.get("attachment")

        if not (fields or attachment):
            return action_result.set_status(phantom.APP_ERROR, "This action requires either the fields or attachment parameter")

        if fields:
            try:
                fields_dict = json.loads(fields)
            except Exception as e:
                return action_result.set_status(phantom.APP_ERROR, f"Could not parse JSON from query_dict parameter: {e}")

            if not isinstance(fields_dict, dict):
                return action_result.set_status(phantom.APP_ERROR, "Could not parse JSON from query_dict parameter")

            field_objs = []
            for field, value in fields_dict.items():
                field_obj = self._client.factory.create("ObjectCommandDataFieldValue")
                field_obj.Name = field
                field_obj.Value = value
                field_objs.append(field_obj)

            field_arr_obj = self._client.factory.create("ArrayOfObjectCommandDataFieldValue")
            field_arr_obj.ObjectCommandDataFieldValue = field_objs

            command_obj = self._client.factory.create("ObjectCommandData")
            command_obj.ObjectType = "Incident#"
            command_obj.Fields = field_arr_obj
            command_obj.ObjectId = ticket_id

            ret_val, response = self._make_soap_call(
                action_result,
                "UpdateObject",
                (
                    self._session_key,
                    self._tenant,
                    command_obj,
                ),
            )

            if phantom.is_fail(ret_val):
                return ret_val

            if response.get("status") == "Error":
                return action_result.set_status(phantom.APP_ERROR, "Could not update the ticket: {}".format(response.get("exceptionReason")))

            if response:
                action_result.add_data(response)

        if attachment:
            attach_result = self._add_attachment(action_result, ticket_id, attachment)
            if not attach_result:
                return attach_result

        return action_result.set_status(phantom.APP_SUCCESS, "Ticket successfully updated")

    def _handle_get_user(self, param):
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")
        self.debug_print(param)

        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        user = param["user"]

        full_obj = self._client.factory.create("RuleClass")
        full_obj._Condition = "="
        full_obj._Join = "OR"
        full_obj._Field = "DisplayName"
        full_obj._Value = user

        login_obj = self._client.factory.create("RuleClass")
        login_obj._Condition = "="
        login_obj._Join = "OR"
        login_obj._Field = "LoginID"
        login_obj._Value = user

        email_obj = self._client.factory.create("RuleClass")
        email_obj._Condition = "="
        email_obj._Join = "OR"
        email_obj._Field = "PrimaryEmail"
        email_obj._Value = user

        rule_arr = self._client.factory.create("ArrayOfRuleClass")
        rule_arr.Rule = [full_obj, login_obj, email_obj]

        select_obj = self._client.factory.create("SelectClass")
        select_obj._All = True

        from_obj = self._client.factory.create("FromClass")
        from_obj._Object = "Employee"

        query_obj = self._client.factory.create("ObjectQueryDefinition")
        query_obj.From = from_obj
        query_obj.Where = rule_arr
        query_obj.Select = select_obj

        ret_val, response = self._make_soap_call(
            action_result,
            "Search",
            (
                self._session_key,
                self._tenant,
                query_obj,
            ),
        )

        if phantom.is_fail(ret_val):
            return ret_val

        if response:
            action_result.add_data(response)

        user_id = (
            response.get("objList", {})
            .get("ArrayOfWebServiceBusinessObject", [{}])[0]
            .get("WebServiceBusinessObject", [{}])[0]
            .get("RecID", "N/A")
        )
        summary = action_result.update_summary({})
        summary["user_rec_id"] = user_id

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_list_users(self, param):
        self.save_progress(f"In action handler for: {self.get_action_identifier()}")
        self.debug_print(param)

        action_result = self.add_action_result(ActionResult(dict(param)))

        ret_val = self._connect(action_result)
        if phantom.is_fail(ret_val):
            return ret_val

        select_obj = self._client.factory.create("SelectClass")
        select_obj._All = True

        from_obj = self._client.factory.create("FromClass")
        from_obj._Object = "Employee"

        query_obj = self._client.factory.create("ObjectQueryDefinition")
        query_obj.From = from_obj
        query_obj.Select = select_obj

        ret_val, response = self._make_soap_call(
            action_result,
            "Search",
            (
                self._session_key,
                self._tenant,
                query_obj,
            ),
        )

        if phantom.is_fail(ret_val):
            return ret_val

        if response:
            action_result.add_data(response)

        num_users = len(response.get("objList", {}).get("ArrayOfWebServiceBusinessObject", []))
        summary = action_result.update_summary({})
        summary["num_users"] = num_users

        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):
        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if action_id == "test_connectivity":
            ret_val = self._handle_test_connectivity(param)
        elif action_id == "on_poll":
            ret_val = self._handle_on_poll(param)
        elif action_id == "run_query":
            ret_val = self._handle_run_query(param)
        elif action_id == "create_ticket":
            ret_val = self._handle_create_ticket(param)
        elif action_id == "update_ticket":
            ret_val = self._handle_update_ticket(param)
        elif action_id == "get_user":
            ret_val = self._handle_get_user(param)
        elif action_id == "list_users":
            ret_val = self._handle_list_users(param)

        return ret_val


if __name__ == "__main__":
    import sys

    # import pudb
    # pudb.set_trace()

    if len(sys.argv) < 2:
        print("No test json specified as input")
        sys.exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = HeatConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)
