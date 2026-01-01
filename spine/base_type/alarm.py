# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.base_type.commondatatypes import TimePeriodElementsType
    from spine.base_type.commondatatypes import TimePeriodType
    from spine.simple_type.alarm import AlarmIdType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.threshold import ThresholdIdType
    from spine.union_type.alarm import AlarmTypeType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import ScopeTypeType



@spine_type('ns_p:AlarmDataType', is_value_type=False, no_attrib_name=False)
class AlarmDataType(SpineBase): # EEBus_SPINE_TS_Alarm.xsd:ns_p:AlarmDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alarm_id",
            "xml_name": "alarmId",
            "type": "ns_p:AlarmIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmIdType"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
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
            "name": "alarm_type",
            "xml_name": "alarmType",
            "type": "ns_p:AlarmTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmTypeType"
        },
        {
            "name": "measured_value",
            "xml_name": "measuredValue",
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
        {
            "name": "evaluation_period",
            "xml_name": "evaluationPeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
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


@spine_type('ns_p:AlarmListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class AlarmListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Alarm.xsd:ns_p:AlarmListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alarm_id",
            "xml_name": "alarmId",
            "type": "ns_p:AlarmIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmIdType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
    ]


@spine_type('ns_p:AlarmListDataType', is_value_type=False, no_attrib_name=False)
class AlarmListDataType(SpineBase): # EEBus_SPINE_TS_Alarm.xsd:ns_p:AlarmListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alarm_data",
            "xml_name": "alarmData",
            "type": "ns_p:AlarmDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "alarm_id",
            "xml_name": "alarmId",
            "type": "ns_p:AlarmIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmIdType"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
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
            "name": "alarm_type",
            "xml_name": "alarmType",
            "type": "ns_p:AlarmTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmTypeType"
        },
        {
            "name": "measured_value",
            "xml_name": "measuredValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "evaluation_period",
            "xml_name": "evaluationPeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
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


@spine_type('ns_p:AlarmDataElementsType', is_value_type=False, no_attrib_name=False)
class AlarmDataElementsType(SpineBase): # EEBus_SPINE_TS_Alarm.xsd:ns_p:AlarmDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alarm_id",
            "xml_name": "alarmId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "alarm_type",
            "xml_name": "alarmType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "measured_value",
            "xml_name": "measuredValue",
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
        {
            "name": "evaluation_period",
            "xml_name": "evaluationPeriod",
            "type": "ns_p:TimePeriodElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodElementsType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
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

