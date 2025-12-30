# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:TariffIdType', is_value_type=True, no_attrib_name=False)
class TariffIdType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffIdType -> AliasType
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


@spine_type('ns_p:IncentiveIdType', is_value_type=True, no_attrib_name=False)
class IncentiveIdType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveIdType -> AliasType
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


@spine_type('ns_p:TierBoundaryIdType', is_value_type=True, no_attrib_name=False)
class TierBoundaryIdType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryIdType -> AliasType
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


@spine_type('ns_p:TierIdType', is_value_type=True, no_attrib_name=False)
class TierIdType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierIdType -> AliasType
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


@spine_type('ns_p:TariffCountType', is_value_type=True, no_attrib_name=False)
class TariffCountType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
    ]


@spine_type('ns_p:IncentiveCountType', is_value_type=True, no_attrib_name=False)
class IncentiveCountType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
    ]


@spine_type('ns_p:TierBoundaryCountType', is_value_type=True, no_attrib_name=False)
class TierBoundaryCountType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
        },
    ]


@spine_type('ns_p:TierCountType', is_value_type=True, no_attrib_name=False)
class TierCountType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
    ]


@spine_type('ns_p:CommodityIdType', is_value_type=True, no_attrib_name=False)
class CommodityIdType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:CommodityIdType -> AliasType
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


@spine_type('ns_p:IncentivePriorityType', is_value_type=True, no_attrib_name=False)
class IncentivePriorityType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentivePriorityType -> AliasType
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

