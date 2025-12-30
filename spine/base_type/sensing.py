# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.base_type.commondatatypes import TimestampIntervalType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.sensing import SensingStateType
    from spine.union_type.sensing import SensingTypeType



@spine_type('ns_p:SensingDataType', is_value_type=False, no_attrib_name=False)
class SensingDataType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:SensingStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingStateType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "number",
            "xml_name": "number",
            "type": "ns_p:NumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NumberType"
        },
        {
            "name": "scale",
            "xml_name": "scale",
            "type": "ns_p:ScaleType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaleType"
        },
    ]


@spine_type('ns_p:SensingDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class SensingDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sensing_type",
            "xml_name": "sensingType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SensingDescriptionDataType', is_value_type=False, no_attrib_name=False)
class SensingDescriptionDataType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sensing_type",
            "xml_name": "sensingType",
            "type": "ns_p:SensingTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingTypeType"
        },
        {
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
        {
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:LabelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LabelType"
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


@spine_type('ns_p:SensingListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SensingListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp_interval",
            "xml_name": "timestampInterval",
            "type": "ns_p:TimestampIntervalType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimestampIntervalType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:SensingListDataType', is_value_type=False, no_attrib_name=False)
class SensingListDataType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sensing_data",
            "xml_name": "sensingData",
            "type": "ns_p:SensingDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:SensingStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingStateType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:SensingDataElementsType', is_value_type=False, no_attrib_name=False)
class SensingDataElementsType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "number",
            "xml_name": "number",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "scale",
            "xml_name": "scale",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

