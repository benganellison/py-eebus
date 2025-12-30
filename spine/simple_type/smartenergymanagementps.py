# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.simple_type.commondatatypes import DescriptionType



@spine_type('ns_p:Anonymous_4504071968', is_value_type=True, no_attrib_name=False)
class Anonymous_4504071968(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504071968 -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]


@spine_type('ns_p:Anonymous_4504021920', is_value_type=True, no_attrib_name=False)
class Anonymous_4504021920(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504021920 -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]

