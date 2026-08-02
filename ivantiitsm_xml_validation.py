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
from __future__ import annotations

import codecs
import re


UNSAFE_XML_DECLARATION = re.compile(r"<!\s*(?:doctype|entity)\b", re.IGNORECASE)


def decode_xml_for_validation(content: bytes) -> str:
    """Decode XML syntax using its BOM or leading-byte encoding signature."""
    if content.startswith(codecs.BOM_UTF8):
        return content.decode("utf-8-sig")
    if content.startswith((codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        return content.decode("utf-32")
    if content.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        return content.decode("utf-16")
    if content.startswith(b"\x00\x00\x00<"):
        return content.decode("utf-32-be")
    if content.startswith(b"<\x00\x00\x00"):
        return content.decode("utf-32-le")
    if content.startswith(b"\x00<"):
        return content.decode("utf-16-be")
    if content.startswith(b"<\x00"):
        return content.decode("utf-16-le")
    return content.decode("utf-8")


def reject_unsafe_xml_declarations(payload: bytes | str) -> None:
    """Reject DTD and entity declarations after decoding XML syntax."""
    if isinstance(payload, str):
        xml_text = payload
    else:
        content = bytes(payload)
        try:
            xml_text = decode_xml_for_validation(content)
        except UnicodeDecodeError:
            xml_text = content.decode("latin-1")
    if UNSAFE_XML_DECLARATION.search(xml_text):
        raise ValueError("Ivanti ITSM XML response contains a prohibited DTD or entity declaration")
