# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:MsgCounterType', is_value_type=True, no_attrib_name=False)
class MsgCounterType(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:MsgCounterType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedLong",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:FilterIdType', is_value_type=True, no_attrib_name=False)
class FilterIdType(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:FilterIdType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]

