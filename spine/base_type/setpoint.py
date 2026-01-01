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
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.measurement import MeasurementIdType
    from spine.simple_type.setpoint import SetpointIdType
    from spine.simple_type.timetable import TimeTableIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.setpoint import SetpointTypeType



@spine_type('ns_p:SetpointDescriptionDataType', is_value_type=False, no_attrib_name=False)
class SetpointDescriptionDataType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "setpoint_type",
            "xml_name": "setpointType",
            "type": "ns_p:SetpointTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointTypeType"
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


@spine_type('ns_p:SetpointConstraintsDataType', is_value_type=False, no_attrib_name=False)
class SetpointConstraintsDataType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "setpoint_range_min",
            "xml_name": "setpointRangeMin",
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
            "name": "setpoint_range_max",
            "xml_name": "setpointRangeMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "setpoint_step_size",
            "xml_name": "setpointStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:SetpointDataType', is_value_type=False, no_attrib_name=False)
class SetpointDataType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
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
        {
            "name": "value_min",
            "xml_name": "valueMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_max",
            "xml_name": "valueMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_tolerance_absolute",
            "xml_name": "valueToleranceAbsolute",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_tolerance_percentage",
            "xml_name": "valueTolerancePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "is_setpoint_changeable",
            "xml_name": "isSetpointChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_setpoint_active",
            "xml_name": "isSetpointActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
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
    ]


@spine_type('ns_p:SetpointDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SetpointDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "setpoint_type",
            "xml_name": "setpointType",
            "type": "ns_p:SetpointTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointTypeType"
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


@spine_type('ns_p:SetpointDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class SetpointDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_description_data",
            "xml_name": "setpointDescriptionData",
            "type": "ns_p:SetpointDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "setpoint_type",
            "xml_name": "setpointType",
            "type": "ns_p:SetpointTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointTypeType"
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


@spine_type('ns_p:SetpointDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class SetpointDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "setpoint_type",
            "xml_name": "setpointType",
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


@spine_type('ns_p:SetpointConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SetpointConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
    ]


@spine_type('ns_p:SetpointConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class SetpointConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_constraints_data",
            "xml_name": "setpointConstraintsData",
            "type": "ns_p:SetpointConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "setpoint_range_min",
            "xml_name": "setpointRangeMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "setpoint_range_max",
            "xml_name": "setpointRangeMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "setpoint_step_size",
            "xml_name": "setpointStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:SetpointConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class SetpointConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "setpoint_range_min",
            "xml_name": "setpointRangeMin",
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
            "name": "setpoint_range_max",
            "xml_name": "setpointRangeMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "setpoint_step_size",
            "xml_name": "setpointStepSize",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:SetpointListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SetpointListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
    ]


@spine_type('ns_p:SetpointListDataType', is_value_type=False, no_attrib_name=False)
class SetpointListDataType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_data",
            "xml_name": "setpointData",
            "type": "ns_p:SetpointDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
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
            "name": "value_min",
            "xml_name": "valueMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_max",
            "xml_name": "valueMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_tolerance_absolute",
            "xml_name": "valueToleranceAbsolute",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_tolerance_percentage",
            "xml_name": "valueTolerancePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "is_setpoint_changeable",
            "xml_name": "isSetpointChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_setpoint_active",
            "xml_name": "isSetpointActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
        },
    ]


@spine_type('ns_p:SetpointDataElementsType', is_value_type=False, no_attrib_name=False)
class SetpointDataElementsType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
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
        {
            "name": "value_min",
            "xml_name": "valueMin",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "value_max",
            "xml_name": "valueMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "value_tolerance_absolute",
            "xml_name": "valueToleranceAbsolute",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "value_tolerance_percentage",
            "xml_name": "valueTolerancePercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "is_setpoint_changeable",
            "xml_name": "isSetpointChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_setpoint_active",
            "xml_name": "isSetpointActive",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
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
    ]

