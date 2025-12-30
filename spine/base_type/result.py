# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.result import ErrorNumberType



@spine_type('ns_p:ResultDataType', is_value_type=False, no_attrib_name=False)
class ResultDataType(SpineBase): # EEBus_SPINE_TS_Result.xsd:ns_p:ResultDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "error_number",
            "xml_name": "errorNumber",
            "type": "ns_p:ErrorNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ErrorNumberType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]

