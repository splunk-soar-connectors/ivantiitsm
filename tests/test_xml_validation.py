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
import pytest

from ivantiitsm_xml_validation import decode_xml_for_validation, reject_unsafe_xml_declarations


@pytest.mark.parametrize("encoding", ["utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be"])
def test_decode_xml_for_validation_recognizes_xml_encodings(encoding):
    xml = "<?xml version='1.0'?><response/>"
    assert decode_xml_for_validation(xml.encode(encoding)) == xml


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be"])
def test_reject_unsafe_xml_declarations_rejects_encoded_dtds(encoding):
    xml = "<?xml version='1.0'?><!DOCTYPE r [<!ENTITY a 'value'>]><r attr='&a;'/>"
    with pytest.raises(ValueError):
        reject_unsafe_xml_declarations(xml.encode(encoding))


def test_reject_unsafe_xml_declarations_accepts_plain_xml():
    reject_unsafe_xml_declarations("<?xml version='1.0'?><response/>")
