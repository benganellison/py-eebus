# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass



@spine_type('ns_p:IncentiveTypeType', is_value_type=True, no_attrib_name=False)
class IncentiveTypeType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveTypeType -> UnionType
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


@spine_type('ns_p:TierBoundaryTypeType', is_value_type=True, no_attrib_name=False)
class TierBoundaryTypeType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryTypeType -> UnionType
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


@spine_type('ns_p:TierTypeType', is_value_type=True, no_attrib_name=False)
class TierTypeType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierTypeType -> UnionType
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


@spine_type('ns_p:IncentiveValueTypeType', is_value_type=True, no_attrib_name=False)
class IncentiveValueTypeType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveValueTypeType -> UnionType
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

