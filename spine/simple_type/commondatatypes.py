# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass


@spine_type('ns_p:SpecificationVersionType', is_value_type=True, no_attrib_name=False)
class SpecificationVersionType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:SpecificationVersionType -> AliasType
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


@spine_type('ns_p:MaxResponseDelayType', is_value_type=True, no_attrib_name=False)
class MaxResponseDelayType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:MaxResponseDelayType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:FeatureGroupType', is_value_type=True, no_attrib_name=False)
class FeatureGroupType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:FeatureGroupType -> AliasType
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


@spine_type('ns_p:AddressFeatureType', is_value_type=True, no_attrib_name=False)
class AddressFeatureType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:AddressFeatureType -> AliasType
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


@spine_type('ns_p:AddressEntityType', is_value_type=True, no_attrib_name=False)
class AddressEntityType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:AddressEntityType -> AliasType
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


@spine_type('ns_p:AddressDeviceType', is_value_type=True, no_attrib_name=False)
class AddressDeviceType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:AddressDeviceType -> AliasType
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


@spine_type('ns_p:CalendarWeekType', is_value_type=True, no_attrib_name=False)
class CalendarWeekType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:CalendarWeekType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedByte",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:DayOfMonthType', is_value_type=True, no_attrib_name=False)
class DayOfMonthType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:DayOfMonthType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedByte",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:DescriptionType', is_value_type=True, no_attrib_name=False)
class DescriptionType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:DescriptionType -> AliasType
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


@spine_type('ns_p:LabelType', is_value_type=True, no_attrib_name=False)
class LabelType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:LabelType -> AliasType
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


@spine_type('ns_p:ScaleType', is_value_type=True, no_attrib_name=False)
class ScaleType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaleType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:short",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:NumberType', is_value_type=True, no_attrib_name=False)
class NumberType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:NumberType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:long",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]

