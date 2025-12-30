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
    from spine.base_type.commondatatypes import TimestampIntervalType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.loadcontrol import LoadControlEventIdType
    from spine.simple_type.loadcontrol import LoadControlLimitIdType
    from spine.simple_type.measurement import MeasurementIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.loadcontrol import LoadControlCategoryType
    from spine.union_type.loadcontrol import LoadControlEventActionType
    from spine.union_type.loadcontrol import LoadControlEventStateType
    from spine.union_type.loadcontrol import LoadControlLimitTypeType



@spine_type('ns_p:LoadControlLimitDescriptionDataType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitDescriptionDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "limit_type",
            "xml_name": "limitType",
            "type": "ns_p:LoadControlLimitTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitTypeType"
        },
        {
            "name": "limit_category",
            "xml_name": "limitCategory",
            "type": "ns_p:LoadControlCategoryType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlCategoryType"
        },
        {
            "name": "limit_direction",
            "xml_name": "limitDirection",
            "type": "ns_p:EnergyDirectionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyDirectionType"
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


@spine_type('ns_p:LoadControlLimitConstraintsDataType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitConstraintsDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "value_range_min",
            "xml_name": "valueRangeMin",
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
            "name": "value_range_max",
            "xml_name": "valueRangeMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_step_size",
            "xml_name": "valueStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:LoadControlLimitDataType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "is_limit_changeable",
            "xml_name": "isLimitChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_limit_active",
            "xml_name": "isLimitActive",
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


@spine_type('ns_p:LoadControlStateDataType', is_value_type=False, no_attrib_name=False)
class LoadControlStateDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateDataType -> ComplexType
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
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
        {
            "name": "event_state_consume",
            "xml_name": "eventStateConsume",
            "type": "ns_p:LoadControlEventStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventStateType"
        },
        {
            "name": "applied_event_action_consume",
            "xml_name": "appliedEventActionConsume",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
        },
        {
            "name": "event_state_produce",
            "xml_name": "eventStateProduce",
            "type": "ns_p:LoadControlEventStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventStateType"
        },
        {
            "name": "applied_event_action_produce",
            "xml_name": "appliedEventActionProduce",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
        },
    ]


@spine_type('ns_p:LoadControlEventDataType', is_value_type=False, no_attrib_name=False)
class LoadControlEventDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventDataType -> ComplexType
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
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
        {
            "name": "event_action_consume",
            "xml_name": "eventActionConsume",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
        },
        {
            "name": "event_action_produce",
            "xml_name": "eventActionProduce",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
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


@spine_type('ns_p:LoadControlLimitDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "limit_type",
            "xml_name": "limitType",
            "type": "ns_p:LoadControlLimitTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitTypeType"
        },
        {
            "name": "limit_direction",
            "xml_name": "limitDirection",
            "type": "ns_p:EnergyDirectionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyDirectionType"
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
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
    ]


@spine_type('ns_p:LoadControlLimitDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "load_control_limit_description_data",
            "xml_name": "loadControlLimitDescriptionData",
            "type": "ns_p:LoadControlLimitDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "limit_type",
            "xml_name": "limitType",
            "type": "ns_p:LoadControlLimitTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitTypeType"
        },
        {
            "name": "limit_category",
            "xml_name": "limitCategory",
            "type": "ns_p:LoadControlCategoryType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlCategoryType"
        },
        {
            "name": "limit_direction",
            "xml_name": "limitDirection",
            "type": "ns_p:EnergyDirectionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyDirectionType"
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


@spine_type('ns_p:LoadControlLimitDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "limit_type",
            "xml_name": "limitType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "limit_category",
            "xml_name": "limitCategory",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "limit_direction",
            "xml_name": "limitDirection",
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


@spine_type('ns_p:LoadControlLimitConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
    ]


@spine_type('ns_p:LoadControlLimitConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "load_control_limit_constraints_data",
            "xml_name": "loadControlLimitConstraintsData",
            "type": "ns_p:LoadControlLimitConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "value_range_min",
            "xml_name": "valueRangeMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_range_max",
            "xml_name": "valueRangeMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_step_size",
            "xml_name": "valueStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:LoadControlLimitConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_range_min",
            "xml_name": "valueRangeMin",
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
            "name": "value_range_max",
            "xml_name": "valueRangeMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "value_step_size",
            "xml_name": "valueStepSize",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:LoadControlLimitListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
    ]


@spine_type('ns_p:LoadControlLimitListDataType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitListDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "load_control_limit_data",
            "xml_name": "loadControlLimitData",
            "type": "ns_p:LoadControlLimitDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:LoadControlLimitIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitIdType"
        },
        {
            "name": "is_limit_changeable",
            "xml_name": "isLimitChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_limit_active",
            "xml_name": "isLimitActive",
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
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:LoadControlLimitDataElementsType', is_value_type=False, no_attrib_name=False)
class LoadControlLimitDataElementsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "limit_id",
            "xml_name": "limitId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_limit_changeable",
            "xml_name": "isLimitChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_limit_active",
            "xml_name": "isLimitActive",
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


@spine_type('ns_p:LoadControlStateListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class LoadControlStateListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateListDataSelectorsType -> ComplexType
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
        {
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
    ]


@spine_type('ns_p:LoadControlStateListDataType', is_value_type=False, no_attrib_name=False)
class LoadControlStateListDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "load_control_state_data",
            "xml_name": "loadControlStateData",
            "type": "ns_p:LoadControlStateDataType",
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
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
        {
            "name": "event_state_consume",
            "xml_name": "eventStateConsume",
            "type": "ns_p:LoadControlEventStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventStateType"
        },
        {
            "name": "applied_event_action_consume",
            "xml_name": "appliedEventActionConsume",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
        },
        {
            "name": "event_state_produce",
            "xml_name": "eventStateProduce",
            "type": "ns_p:LoadControlEventStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventStateType"
        },
        {
            "name": "applied_event_action_produce",
            "xml_name": "appliedEventActionProduce",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
        },
    ]


@spine_type('ns_p:LoadControlStateDataElementsType', is_value_type=False, no_attrib_name=False)
class LoadControlStateDataElementsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateDataElementsType -> ComplexType
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
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "event_state_consume",
            "xml_name": "eventStateConsume",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "applied_event_action_consume",
            "xml_name": "appliedEventActionConsume",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "event_state_produce",
            "xml_name": "eventStateProduce",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "applied_event_action_produce",
            "xml_name": "appliedEventActionProduce",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:LoadControlEventListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class LoadControlEventListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventListDataSelectorsType -> ComplexType
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
        {
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
    ]


@spine_type('ns_p:LoadControlEventListDataType', is_value_type=False, no_attrib_name=False)
class LoadControlEventListDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "load_control_event_data",
            "xml_name": "loadControlEventData",
            "type": "ns_p:LoadControlEventDataType",
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
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
        {
            "name": "event_action_consume",
            "xml_name": "eventActionConsume",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
        },
        {
            "name": "event_action_produce",
            "xml_name": "eventActionProduce",
            "type": "ns_p:LoadControlEventActionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventActionType"
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


@spine_type('ns_p:LoadControlEventDataElementsType', is_value_type=False, no_attrib_name=False)
class LoadControlEventDataElementsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventDataElementsType -> ComplexType
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
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "event_action_consume",
            "xml_name": "eventActionConsume",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "event_action_produce",
            "xml_name": "eventActionProduce",
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


@spine_type('ns_p:LoadControlNodeDataElementsType', is_value_type=False, no_attrib_name=False)
class LoadControlNodeDataElementsType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlNodeDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "is_node_remote_controllable",
            "xml_name": "isNodeRemoteControllable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:LoadControlNodeDataType', is_value_type=False, no_attrib_name=False)
class LoadControlNodeDataType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlNodeDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "is_node_remote_controllable",
            "xml_name": "isNodeRemoteControllable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]

