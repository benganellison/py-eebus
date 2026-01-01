# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:ChannelIdType', is_value_type=True, no_attrib_name=False)
class ChannelIdType(SpineBase): # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:ChannelIdType -> AliasType
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


@spine_type('ns_p:PurposeIdType', is_value_type=True, no_attrib_name=False)
class PurposeIdType(SpineBase): # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:PurposeIdType -> AliasType
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

