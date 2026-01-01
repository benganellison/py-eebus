# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:MessagingDataTextType', is_value_type=True, no_attrib_name=False)
class MessagingDataTextType(SpineBase): # EEBus_SPINE_TS_Messaging.xsd:ns_p:MessagingDataTextType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:MessagingNumberType', is_value_type=True, no_attrib_name=False)
class MessagingNumberType(SpineBase): # EEBus_SPINE_TS_Messaging.xsd:ns_p:MessagingNumberType -> AliasType
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

