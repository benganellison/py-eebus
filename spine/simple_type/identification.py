# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass



@spine_type('ns_p:IdentificationValueType', is_value_type=True, no_attrib_name=False)
class IdentificationValueType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationValueType -> AliasType
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


@spine_type('ns_p:IdentificationIdType', is_value_type=True, no_attrib_name=False)
class IdentificationIdType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationIdType -> AliasType
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


@spine_type('ns_p:SessionIdType', is_value_type=True, no_attrib_name=False)
class SessionIdType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdType -> AliasType
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

