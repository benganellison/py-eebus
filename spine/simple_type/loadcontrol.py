# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass


@spine_type('ns_p:LoadControlLimitIdType', is_value_type=True, no_attrib_name=False)
class LoadControlLimitIdType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitIdType -> AliasType
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


@spine_type('ns_p:LoadControlEventIdType', is_value_type=True, no_attrib_name=False)
class LoadControlEventIdType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventIdType -> AliasType
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

