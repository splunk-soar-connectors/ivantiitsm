[comment]: # "Auto-generated SOAR connector documentation"
# Ivanti ITSM

Publisher: Splunk  
Connector Version: 2\.1\.2  
Product Vendor: Ivanti  
Product Name: ITSM  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.10\.0\.40961  

This app integrates with Ivanti ITSM to provide ingestion and several ticketing actions

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a ITSM asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**url** |  required  | string | Server URL
**username** |  required  | string | Username
**password** |  required  | password | Password
**poll\_now\_ingestion\_span** |  required  | numeric | Poll last n days for 'Poll Now'
**first\_scheduled\_ingestion\_span** |  required  | numeric | Poll last n days for first scheduled polling

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[create ticket](#action-create-ticket) - Create a new ticket  
[update ticket](#action-update-ticket) - Update a ticket  
[run query](#action-run-query) - Search for a text in resources  
[on poll](#action-on-poll) - Ingest latest tickets  
[get user](#action-get-user) - Get information about a user  
[list users](#action-list-users) - List all users on system  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'create ticket'
Create a new ticket

Type: **generic**  
Read only: **False**

Certain fields are required to create a ticket on Help Desk\. Those fields are represented by the required parameters for this action\.<br><br>The <b>customer</b> parameter takes a Customer Record ID, which can be found by running a <b>list users</b> or a <b>get user</b> action\.<br><br>The <b>fields</b> parameter takes a JSON dictionary containing other fields and values that can be set during ticket creation\. For example\:<br>\{<br>    &quot;Impact&quot;\: &quot;High&quot;<br>    &quot;Urgency&quot;\: &quot;Medium&quot;<br>\}</pre><br><br>The <b>attachment</b> parameter takes a vault ID\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**summary** |  required  | Summary | string | 
**description** |  required  | Description | string | 
**service** |  required  | Service | string | 
**category** |  required  | Category | string | 
**customer** |  required  | Customer Record ID | string |  `ivanti user id` 
**fields** |  optional  | JSON containing field values | string | 
**attachment** |  optional  | Vault ID of file to attach | string |  `vault id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.attachment | string |  `vault id` 
action\_result\.parameter\.category | string | 
action\_result\.parameter\.customer | string |  `ivanti user id` 
action\_result\.parameter\.description | string | 
action\_result\.parameter\.fields | string | 
action\_result\.parameter\.service | string | 
action\_result\.parameter\.summary | string | 
action\_result\.data\.\*\.obj\.Alias | string | 
action\_result\.data\.\*\.obj\.BusinessObjectName | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualCategory | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualCategory\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualService | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualService\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.AddChatconversationtoActivityHistory | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactEmail | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactPhone | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ApprovalStatus | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Approver | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.Approver\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Category\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.CauseCode | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CauseCode\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosedDuration | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosingEscLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosingEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosingEscLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Cost | numeric | 
action\_result\.data\.\*\.obj\.FieldValues\.CostPerMinute | numeric | 
action\_result\.data\.\*\.obj\.FieldValues\.CostPerMinute\_Currency | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CostPerMinute\_CurrencyValid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Cost\_Currency | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Cost\_CurrencyValid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CreatedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CreatedByType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CreatedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CustomerDepartment | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CustomerLocation | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CustomerLocation\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Email | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.EntityLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.EntityLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.EntityLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.EventCIRecId | string | 
action\_result\.data\.\*\.obj\.FieldValues\.FirstCallResolution | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.HRCaseLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HRCaseLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HRCaseLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HoursOfOperation | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HoursOfOperation\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Impact | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Impact\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentDetailSummary | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentDetailWorkflowTag | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentNetworkUserName | string |  `user name` 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentNumber | numeric | 
action\_result\.data\.\*\.obj\.FieldValues\.IsApprovalNeeded | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsDSMTaskExisted | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsInFinalState | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsMasterIncident | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsNewRecord | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsNotification | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsReclassifiedForResolution | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsRelatedIncidentResolutionUpdate | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsRelatedIncidentUpdate | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsReportedByAlternateContact | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsResolvedByMaster | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsUnRead | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsVIP | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsWorkAround | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.KnowledgeLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.KnowledgeLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.KnowledgeLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.LastModBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.LastModDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.LoginId | string | 
action\_result\.data\.\*\.obj\.FieldValues\.MasterIncidentLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.MasterIncidentLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.MasterIncidentLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.NewNotes | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OrgUnitLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OrgUnitLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OrgUnitLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OrganizationUnitID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Owner | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerTeam | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerTeamEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerTeam\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Owner\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnershipAssignmentEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.OwningOrgUnitId | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OwningOrgUnitId\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Phone | string | 
action\_result\.data\.\*\.obj\.FieldValues\.PreviousState | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Priority | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Priority\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ProblemLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProblemLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProblemLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileFullName | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ProgressBarPosition | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ReadOnly | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.RecId | string |  `ivanti ticket id` 
action\_result\.data\.\*\.obj\.FieldValues\.ReportedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ReportingOrgUnitID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ReportingOrgUnitID\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Resolution | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolutionEscLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolutionEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolutionEscLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedByIncidentNumber | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedByType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.RespondedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.RespondedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResponseEscLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResponseEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResponseEscLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLA | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLADisplayText | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLALink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLALink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLALink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SendSurveyNotification | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.Service | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceOwnerEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceReqLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceReqLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceReqLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Service\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.SocialTextHeader | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Source | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Source\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Status | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Status\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Subcategory | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Subcategory\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Subject | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Symptom | string | 
action\_result\.data\.\*\.obj\.FieldValues\.TeamManagerEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.TotalTimeSpent | string | 
action\_result\.data\.\*\.obj\.FieldValues\.TypeOfIncident | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Urgency | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Urgency\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ViewType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.WaitingEscLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.WaitingEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.WaitingEscLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.helpdesk\_Priority | string | 
action\_result\.data\.\*\.obj\.FieldValues\.helpdesk\_Priority\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_RequestforInformationorData | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_TeamsUserDetailsLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_TeamsUserDetailsLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_TeamsUserDetailsLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_UpdateRFI | string | 
action\_result\.data\.\*\.obj\.RecID | string |  `md5`  `ivanti ticket id` 
action\_result\.data\.\*\.obj\.TableRef | string | 
action\_result\.data\.\*\.recId | string |  `md5` 
action\_result\.data\.\*\.status | string | 
action\_result\.summary\.created\_ticket\_id | string |  `md5` 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update ticket'
Update a ticket

Type: **generic**  
Read only: **False**

The <b>fields</b> parameter takes a JSON dictionary containing fields and values that can be updated with this action\. For example\:<br>\{<br>    &quot;Impact&quot;\: &quot;High&quot;<br>    &quot;Urgency&quot;\: &quot;Medium&quot;<br>\}</pre><br><br>The <b>attachment</b> parameter takes a vault ID\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Incident Record ID | string |  `ivanti ticket id` 
**fields** |  optional  | JSON containing field values | string | 
**attachment** |  optional  | Vault ID of file to attach | string |  `vault id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.attachment | string |  `vault id` 
action\_result\.parameter\.fields | string | 
action\_result\.parameter\.id | string |  `ivanti ticket id` 
action\_result\.data\.\*\.exceptionReason | string | 
action\_result\.data\.\*\.obj\.Alias | string | 
action\_result\.data\.\*\.obj\.BusinessObjectName | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualCategory | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualCategory\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualService | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ActualService\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.AddChatconversationtoActivityHistory | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactEmail | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.AlternateContactPhone | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ApprovalStatus | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Approver | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Approver\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Category\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.CauseCode | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CauseCode\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosedDuration | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosingEscLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ClosingEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ClosingEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Cost | numeric | 
action\_result\.data\.\*\.obj\.FieldValues\.CostPerMinute | numeric | 
action\_result\.data\.\*\.obj\.FieldValues\.CostPerMinute\_Currency | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CostPerMinute\_CurrencyValid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Cost\_Currency | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Cost\_CurrencyValid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CreatedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CreatedByType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CreatedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CustomerDepartment | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CustomerLocation | string | 
action\_result\.data\.\*\.obj\.FieldValues\.CustomerLocation\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Email | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.EntityLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.EntityLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.EntityLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.EventCIRecId | string | 
action\_result\.data\.\*\.obj\.FieldValues\.FirstCallResolution | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.HRCaseLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HRCaseLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HRCaseLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HoursOfOperation | string | 
action\_result\.data\.\*\.obj\.FieldValues\.HoursOfOperation\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Impact | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Impact\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentDetailSummary | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentDetailWorkflowTag | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentNetworkUserName | string |  `user name` 
action\_result\.data\.\*\.obj\.FieldValues\.IncidentNumber | numeric | 
action\_result\.data\.\*\.obj\.FieldValues\.IsApprovalNeeded | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsDSMTaskExisted | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsInFinalState | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsMasterIncident | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsNewRecord | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsNotification | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsReclassifiedForResolution | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsRelatedIncidentResolutionUpdate | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsRelatedIncidentUpdate | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsReportedByAlternateContact | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsResolvedByMaster | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsUnRead | string | 
action\_result\.data\.\*\.obj\.FieldValues\.IsVIP | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.IsWorkAround | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.KnowledgeLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.KnowledgeLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.KnowledgeLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.LastModBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.LastModDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.LoginId | string | 
action\_result\.data\.\*\.obj\.FieldValues\.MasterIncidentLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.MasterIncidentLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.MasterIncidentLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.NewNotes | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OrgUnitLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OrgUnitLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OrgUnitLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OrganizationUnitID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Owner | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerTeam | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerTeamEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerTeam\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnerType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Owner\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.OwnershipAssignmentEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.OwningOrgUnitId | string | 
action\_result\.data\.\*\.obj\.FieldValues\.OwningOrgUnitId\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Phone | string | 
action\_result\.data\.\*\.obj\.FieldValues\.PreviousState | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Priority | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Priority\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ProblemLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProblemLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProblemLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileFullName | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ProfileLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ProgressBarPosition | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ReadOnly | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.RecId | string |  `ivanti ticket id` 
action\_result\.data\.\*\.obj\.FieldValues\.ReportedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ReportingOrgUnitID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ReportingOrgUnitID\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Resolution | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolutionEscLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ResolutionEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolutionEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedByIncidentNumber | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedByType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResolvedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.RespondedBy | string | 
action\_result\.data\.\*\.obj\.FieldValues\.RespondedDateTime | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResponseEscLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ResponseEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ResponseEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.SLA | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLADisplayText | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLALink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLALink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SLALink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.SendSurveyNotification | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.Service | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceOwnerEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceReqLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceReqLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ServiceReqLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Service\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.SocialTextHeader | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Source | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Source\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Status | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Status\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.Subcategory | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Subcategory\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Subject | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Symptom | string | 
action\_result\.data\.\*\.obj\.FieldValues\.TeamManagerEmail | string |  `email` 
action\_result\.data\.\*\.obj\.FieldValues\.TotalTimeSpent | string | 
action\_result\.data\.\*\.obj\.FieldValues\.TypeOfIncident | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Urgency | string | 
action\_result\.data\.\*\.obj\.FieldValues\.Urgency\_Valid | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.ViewType | string | 
action\_result\.data\.\*\.obj\.FieldValues\.WaitingEscLink | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.WaitingEscLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.WaitingEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.obj\.FieldValues\.helpdesk\_Priority | string | 
action\_result\.data\.\*\.obj\.FieldValues\.helpdesk\_Priority\_Valid | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_RequestforInformationorData | boolean | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_TeamsUserDetailsLink | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_TeamsUserDetailsLink\_Category | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_TeamsUserDetailsLink\_RecID | string | 
action\_result\.data\.\*\.obj\.FieldValues\.ivnt\_UpdateRFI | string | 
action\_result\.data\.\*\.obj\.RecID | string |  `md5`  `ivanti ticket id` 
action\_result\.data\.\*\.obj\.TableRef | string | 
action\_result\.data\.\*\.recId | string |  `ivanti ticket id` 
action\_result\.data\.\*\.status | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'run query'
Search for a text in resources

Type: **investigate**  
Read only: **True**

The <b>query\_dict</b> parameter takes a JSON dictionary with each key representing a field in an event to query\. See the <b>LogQueryFilterTypeEnum</b> section of the <b>LogRhythm® SOAP API Reference Guide</b> for a list of event fields that can be queried\.<br><br>This action requires one of the parameters to run\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**from\_date** |  optional  | Start Date \(YYYY\-MM\-DD hh\:mm\:ss\) | string | 
**to\_date** |  optional  | End Date \(YYYY\-MM\-DD hh\:mm\:ss\) | string | 
**query\_dict** |  optional  | Query Dictionary | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.from\_date | string | 
action\_result\.parameter\.query\_dict | string | 
action\_result\.parameter\.to\_date | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.Alias | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.BusinessObjectName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ActualCategory | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ActualCategory\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ActualService | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ActualService\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AddChatconversationtoActivityHistory | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AlternateContactEmail | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AlternateContactLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AlternateContactLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AlternateContactLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AlternateContactPhone | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ApprovalStatus | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Approver | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Approver\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Category\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CauseCode | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CauseCode\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ClosedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ClosedDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ClosedDuration | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ClosingEscLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ClosingEscLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ClosingEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Cost | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CostPerMinute | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CostPerMinute\_Currency | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CostPerMinute\_CurrencyValid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Cost\_Currency | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Cost\_CurrencyValid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedByType | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CustomerDepartment | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CustomerLocation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CustomerLocation\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Email | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EventCIRecId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.FirstCallResolution | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HRCaseLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HRCaseLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HRCaseLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HoursOfOperation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HoursOfOperation\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Impact | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Impact\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IncidentDetailSummary | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IncidentDetailWorkflowTag | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IncidentNetworkUserName | string |  `user name` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IncidentNumber | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsApprovalNeeded | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsDSMTaskExisted | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsInFinalState | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsMasterIncident | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsNewRecord | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsNotification | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsReclassifiedForResolution | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsRelatedIncidentResolutionUpdate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsRelatedIncidentUpdate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsReportedByAlternateContact | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsResolvedByMaster | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsUnRead | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsVIP | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsWorkAround | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.KnowledgeLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.KnowledgeLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.KnowledgeLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastModBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastModDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.MasterIncidentLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.MasterIncidentLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.MasterIncidentLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NewNotes | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrganizationUnitID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Owner | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwnerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwnerTeam | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwnerTeamEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwnerTeam\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwnerType | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Owner\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwnershipAssignmentEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwningOrgUnitId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OwningOrgUnitId\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PreviousState | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Priority | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Priority\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProblemLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProblemLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProblemLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProfileFullName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProfileLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProfileLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProfileLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProgressBarPosition | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReadOnly | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RecId | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportingOrgUnitID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportingOrgUnitID\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Resolution | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolutionEscLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolutionEscLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolutionEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolvedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolvedByIncidentNumber | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolvedByType | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResolvedDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RespondedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RespondedDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResponseEscLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResponseEscLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ResponseEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLA | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLADisplayText | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLALink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLALink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLALink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SendSurveyNotification | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Service | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ServiceOwnerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ServiceReqLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ServiceReqLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ServiceReqLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Service\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SocialTextHeader | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Source | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Source\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Status | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Status\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Subcategory | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Subcategory\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Subject | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Symptom | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TeamManagerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TotalTimeSpent | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TypeOfIncident | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Urgency | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Urgency\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ViewType | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.WaitingEscLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.WaitingEscLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.WaitingEscLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.helpdesk\_Priority | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.helpdesk\_Priority\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_RequestforInformationorData | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_TeamsUserDetailsLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_TeamsUserDetailsLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_TeamsUserDetailsLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateRFI | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.TableRef | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.summary\.num\_tickets | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'on poll'
Ingest latest tickets

Type: **ingest**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**container\_id** |  optional  | Parameter ignored in this app | numeric | 
**start\_time** |  optional  | Parameter ignored in this app | numeric | 
**end\_time** |  optional  | Parameter ignored in this app | numeric | 
**container\_count** |  optional  | Parameter ignored in this app | numeric | 
**artifact\_count** |  optional  | Parameter ignored in this app | numeric | 

#### Action Output
No Output  

## action: 'get user'
Get information about a user

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user** |  required  | User login, email, or full name | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.user | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.Alias | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.BusinessObjectName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AccessListOrgUnit | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1City | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1Country | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1Line2 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1State | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1Zip | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Birthdate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.BuildingName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.BusinessUnit | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.BusinessUnitID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ContactId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CostCentre | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreationMethod | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreationMethod\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreationSource | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CustID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DN | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DefaultChargingAccount | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DefaultChargingAccount\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Department | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DepartmentCode | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Department\_Sync | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Department\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Disabled | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DisplayName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Emp\_LoginId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeeInformation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeeLocation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeeLocation\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeePhoto | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeePhotoName | string |  `file path` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeePhotoRevision | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EnableIPCMIntegration | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.FirstName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Floor | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.GlobalId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HiredDate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_AgentGroup | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_AgentGroup\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_Audited | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_Audited\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_Description | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_EnableIPCMUser | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialAgentStatus | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialAgentStatus\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialNotReadyReason | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialNotReadyReason\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_NotReadyRequired | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_NotReadyRequired\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_OverrideDN | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_RecordingPct | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_SearchableByName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_UILanguage | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_UILanguage\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VOIPLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VOIPLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VOIPLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VoiceAgent | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VoiceSupervisor | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_WrapupSeconds | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_WrapupTimeout | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_WrapupTimeout\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IVRPinCode | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IdentityId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InitialNotReadyReasonValue | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InitialNotReadyReasonValue\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InternalAuthPasswd | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InternalPwdDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsAutoProvisioned | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsExternalAuth | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsInternalAuth | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsNamedUser | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Language | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Language\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastExternalLoginId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastModBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastModDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LocationLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LocationLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LocationLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LockDate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LockType | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginAttemptCount | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginId\_Name | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.MiddleName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NamedLicenseBundle | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NamedLicenseBundle\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NetworkUserName | string |  `user name` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NotificationLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NotificationLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NotificationLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrganizationalUnit | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Owner | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Owner\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ParentLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ParentLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ParentLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PasswordExpiration | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone1 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone1Ext | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone2 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone2Ext | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Prefix | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Prefix\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PrimaryEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PrimaryPhone | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProfileID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReadOnly | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RecId | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RegionLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RegionLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RegionLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RemoteControlPwd | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RemoteControlUID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedByLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedByLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedByLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Room | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLAClass | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLAClass\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Status | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Status\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Suffix | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Suffix\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Supervisor | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Team | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TeamEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TeamManagerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Team\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TempInternalAuthPassword | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TempPwdDatetime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TerminatedDate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Title | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Title\_Sync | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Title\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.VIP | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.WeeklyAvailability | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_Country | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleNumber | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CurrencyText | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_Director | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_HRCaseLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_HRCaseLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_HRCaseLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateBuilding | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateBuilding\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateFloor | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateFloor\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateLocation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateLocation\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_WorkOrderlink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_WorkOrderlink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_WorkOrderlink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.RecID | string |  `ivanti user id` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.TableRef | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.summary\.user\_rec\_id | string |  `md5` 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list users'
List all users on system

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.Alias | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.BusinessObjectName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.AccessListOrgUnit | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1City | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1Country | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1Line2 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1State | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Address1Zip | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Birthdate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.BuildingName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.BusinessUnit | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.BusinessUnitID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ContactId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CostCentre | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreatedDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreationMethod | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreationMethod\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CreationSource | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.CustID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DN | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DefaultChargingAccount | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DefaultChargingAccount\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Department | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DepartmentCode | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Department\_Sync | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Department\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Disabled | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.DisplayName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Emp\_LoginId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeeInformation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeeLocation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeeLocation\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeePhoto | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeePhotoName | string |  `file path` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EmployeePhotoRevision | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EnableIPCMIntegration | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.EntityLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.FirstName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Floor | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.GlobalId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.HiredDate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_AgentGroup | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_AgentGroup\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_Audited | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_Audited\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_Description | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_EnableIPCMUser | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialAgentStatus | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialAgentStatus\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialNotReadyReason | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_InitialNotReadyReason\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_NotReadyRequired | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_NotReadyRequired\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_OverrideDN | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_RecordingPct | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_SearchableByName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_UILanguage | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_UILanguage\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VOIPLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VOIPLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VOIPLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VoiceAgent | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_VoiceSupervisor | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_WrapupSeconds | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_WrapupTimeout | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IPCM\_WrapupTimeout\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IVRPinCode | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IdentityId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InitialNotReadyReasonValue | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InitialNotReadyReasonValue\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InternalAuthPasswd | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.InternalPwdDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsAutoProvisioned | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsExternalAuth | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsInternalAuth | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.IsNamedUser | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Language | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Language\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastExternalLoginId | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastModBy | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastModDateTime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LastName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LocationLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LocationLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LocationLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LockDate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LockType | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginAttemptCount | numeric | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.LoginId\_Name | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ManagerLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.MiddleName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NamedLicenseBundle | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NamedLicenseBundle\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NetworkUserName | string |  `user name` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NotificationLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NotificationLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.NotificationLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrgUnitLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.OrganizationalUnit | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Owner | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Owner\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ParentLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ParentLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ParentLink\_RecID | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PasswordExpiration | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone1 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone1Ext | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone2 | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Phone2Ext | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Prefix | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Prefix\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PrimaryEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.PrimaryPhone | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ProfileID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReadOnly | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RecId | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RegionLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RegionLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RegionLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RemoteControlPwd | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.RemoteControlUID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedByLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedByLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ReportedByLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Room | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLAClass | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.SLAClass\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Status | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Status\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Suffix | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Suffix\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Supervisor | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Team | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TeamEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TeamManagerEmail | string |  `email` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Team\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TempInternalAuthPassword | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TempPwdDatetime | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.TerminatedDate | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Title | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Title\_Sync | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.Title\_Valid | string |  `md5` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.VIP | boolean | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.WeeklyAvailability | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_BuildingName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_Country | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CubicleNumber | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_CurrencyText | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_Director | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_FloorName | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_HRCaseLink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_HRCaseLink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_HRCaseLink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateBuilding | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateBuilding\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateFloor | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateFloor\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateLocation | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_UpdateLocation\_Valid | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_WorkOrderlink | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_WorkOrderlink\_Category | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.FieldValues\.ivnt\_WorkOrderlink\_RecID | string | 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.RecID | string |  `ivanti user id` 
action\_result\.data\.\*\.objList\.ArrayOfWebServiceBusinessObject\.\*\.WebServiceBusinessObject\.\*\.TableRef | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.summary\.num\_users | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 