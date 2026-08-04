# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
from unittest import mock

from ivantiitsm_xml_validation import LimitedXmlResponse, decode_xml_for_validation, reject_unsafe_xml_declarations


class XmlValidationTest(unittest.TestCase):
    def test_recognizes_xml_encodings(self):
        xml = "<?xml version='1.0'?><response/>"
        encodings = ("utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be")
        for encoding in encodings:
            with self.subTest(encoding=encoding):
                self.assertEqual(decode_xml_for_validation(xml.encode(encoding)), xml)

    def test_rejects_encoded_dtds(self):
        xml = "<?xml version='1.0'?><!DOCTYPE r [<!ENTITY a 'value'>]><r attr='&a;'/>"
        encodings = ("utf-8", "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be")
        for encoding in encodings:
            with self.subTest(encoding=encoding), self.assertRaises(ValueError):
                reject_unsafe_xml_declarations(xml.encode(encoding))

    def test_rejects_bomless_encoded_dtds_after_leading_whitespace(self):
        xml = " \n<!DOCTYPE r [<!ENTITY a 'value'>]><r attr='&a;'/>"
        for encoding in ("utf-16-le", "utf-16-be", "utf-32-le", "utf-32-be"):
            with self.subTest(encoding=encoding), self.assertRaises(ValueError):
                reject_unsafe_xml_declarations(xml.encode(encoding))

    def test_accepts_plain_xml(self):
        reject_unsafe_xml_declarations("<?xml version='1.0'?><response/>")

    def test_limited_response_rejects_declaration_before_returning_content(self):
        response = mock.Mock()
        response.read.return_value = b'<!DOCTYPE x [<!ENTITY a "x">]><x>&a;</x>'
        limited = LimitedXmlResponse(response, 1024)

        with self.assertRaisesRegex(ValueError, "prohibited DTD"):
            limited.read()

    def test_rejects_malformed_utf16_instead_of_falling_back(self):
        xml = "<?xml version='1.0'?><!DOCTYPE r [<!ENTITY a 'value'>]><r>&a;</r>"
        malformed = xml.encode("utf-16") + b"\x00"

        with self.assertRaisesRegex(ValueError, "invalid or unsupported encoding"):
            reject_unsafe_xml_declarations(malformed)
