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


class LimitedXmlResponse:
    """Bound and validate a suds response before its XML parser receives it."""

    def __init__(self, response, max_bytes: int):
        self._response = response
        self._max_bytes = max_bytes
        self._content = bytearray()

    def __getattr__(self, name):
        return getattr(self._response, name)

    def read(self, size=None):
        remaining = self._max_bytes - len(self._content)
        read_size = remaining + 1 if size is None else min(size, remaining + 1)
        content = self._response.read(read_size)
        self._content.extend(content)
        if len(self._content) > self._max_bytes:
            raise ValueError("Ivanti ITSM XML response exceeds the 16 MiB safety limit")
        reject_unsafe_xml_declarations(self._content)
        return content


def decode_xml_for_validation(content: bytes) -> str:
    """Decode XML syntax using its BOM or leading-byte encoding signature."""
    if content.startswith(codecs.BOM_UTF8):
        return content.decode("utf-8-sig")
    if content.startswith((codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        return content.decode("utf-32")
    if content.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        return content.decode("utf-16")
    if len(content) >= 4 and content[:3] == b"\x00\x00\x00" and content[3] != 0:
        return content.decode("utf-32-be")
    if len(content) >= 4 and content[0] != 0 and content[1:4] == b"\x00\x00\x00":
        return content.decode("utf-32-le")
    if len(content) >= 2 and content[0] == 0 and content[1] != 0:
        return content.decode("utf-16-be")
    if len(content) >= 2 and content[0] != 0 and content[1] == 0:
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
        except UnicodeDecodeError as error:
            raise ValueError("Ivanti ITSM XML response uses an invalid or unsupported encoding") from error
    if UNSAFE_XML_DECLARATION.search(xml_text):
        raise ValueError("Ivanti ITSM XML response contains a prohibited DTD or entity declaration")
