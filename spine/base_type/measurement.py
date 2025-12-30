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
    from spine.simple_type.measurement import MeasurementIdType
    from spine.simple_type.threshold import ThresholdIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CommodityTypeType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.measurement import MeasurementTypeType
    from spine.union_type.measurement import MeasurementValueSourceType
    from spine.union_type.measurement import MeasurementValueStateType
    from spine.union_type.measurement import MeasurementValueTendencyType
    from spine.union_type.measurement import MeasurementValueTypeType



@spine_type('ns_p:MeasurementThresholdRelationDataType', is_value_type=False, no_attrib_name=False)
class MeasurementThresholdRelationDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementThresholdRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:MeasurementDescriptionDataType', is_value_type=False, no_attrib_name=False)
class MeasurementDescriptionDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "measurement_type",
            "xml_name": "measurementType",
            "type": "ns_p:MeasurementTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementTypeType"
        },
        {
            "name": "commodity_type",
            "xml_name": "commodityType",
            "type": "ns_p:CommodityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityTypeType"
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
            "name": "calibration_value",
            "xml_name": "calibrationValue",
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


@spine_type('ns_p:MeasurementConstraintsDataType', is_value_type=False, no_attrib_name=False)
class MeasurementConstraintsDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
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


@spine_type('ns_p:MeasurementSeriesDataType', is_value_type=False, no_attrib_name=False)
class MeasurementSeriesDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementSeriesDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:MeasurementValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTypeType"
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
            "name": "value_source",
            "xml_name": "valueSource",
            "type": "ns_p:MeasurementValueSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueSourceType"
        },
        {
            "name": "value_tendency",
            "xml_name": "valueTendency",
            "type": "ns_p:MeasurementValueTendencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTendencyType"
        },
        {
            "name": "value_state",
            "xml_name": "valueState",
            "type": "ns_p:MeasurementValueStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueStateType"
        },
    ]


@spine_type('ns_p:MeasurementDataType', is_value_type=False, no_attrib_name=False)
class MeasurementDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:MeasurementValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTypeType"
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
            "name": "value_source",
            "xml_name": "valueSource",
            "type": "ns_p:MeasurementValueSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueSourceType"
        },
        {
            "name": "value_tendency",
            "xml_name": "valueTendency",
            "type": "ns_p:MeasurementValueTendencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTendencyType"
        },
        {
            "name": "value_state",
            "xml_name": "valueState",
            "type": "ns_p:MeasurementValueStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueStateType"
        },
    ]


@spine_type('ns_p:MeasurementThresholdRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class MeasurementThresholdRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementThresholdRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
    ]


@spine_type('ns_p:MeasurementThresholdRelationListDataType', is_value_type=False, no_attrib_name=False)
class MeasurementThresholdRelationListDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementThresholdRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_threshold_relation_data",
            "xml_name": "measurementThresholdRelationData",
            "type": "ns_p:MeasurementThresholdRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:MeasurementThresholdRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class MeasurementThresholdRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementThresholdRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
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
    ]


@spine_type('ns_p:MeasurementDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class MeasurementDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "measurement_type",
            "xml_name": "measurementType",
            "type": "ns_p:MeasurementTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementTypeType"
        },
        {
            "name": "commodity_type",
            "xml_name": "commodityType",
            "type": "ns_p:CommodityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityTypeType"
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


@spine_type('ns_p:MeasurementDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class MeasurementDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_description_data",
            "xml_name": "measurementDescriptionData",
            "type": "ns_p:MeasurementDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "measurement_type",
            "xml_name": "measurementType",
            "type": "ns_p:MeasurementTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementTypeType"
        },
        {
            "name": "commodity_type",
            "xml_name": "commodityType",
            "type": "ns_p:CommodityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityTypeType"
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
            "name": "calibration_value",
            "xml_name": "calibrationValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
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


@spine_type('ns_p:MeasurementDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class MeasurementDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "measurement_type",
            "xml_name": "measurementType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "commodity_type",
            "xml_name": "commodityType",
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
            "name": "calibration_value",
            "xml_name": "calibrationValue",
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


@spine_type('ns_p:MeasurementConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class MeasurementConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
    ]


@spine_type('ns_p:MeasurementConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class MeasurementConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_constraints_data",
            "xml_name": "measurementConstraintsData",
            "type": "ns_p:MeasurementConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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


@spine_type('ns_p:MeasurementConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class MeasurementConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
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


@spine_type('ns_p:MeasurementSeriesListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class MeasurementSeriesListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementSeriesListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:MeasurementValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTypeType"
        },
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


@spine_type('ns_p:MeasurementSeriesListDataType', is_value_type=False, no_attrib_name=False)
class MeasurementSeriesListDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementSeriesListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_series_data",
            "xml_name": "measurementSeriesData",
            "type": "ns_p:MeasurementSeriesDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:MeasurementValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTypeType"
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_source",
            "xml_name": "valueSource",
            "type": "ns_p:MeasurementValueSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueSourceType"
        },
        {
            "name": "value_tendency",
            "xml_name": "valueTendency",
            "type": "ns_p:MeasurementValueTendencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTendencyType"
        },
        {
            "name": "value_state",
            "xml_name": "valueState",
            "type": "ns_p:MeasurementValueStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueStateType"
        },
    ]


@spine_type('ns_p:MeasurementSeriesDataElementsType', is_value_type=False, no_attrib_name=False)
class MeasurementSeriesDataElementsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementSeriesDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
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
            "name": "value_source",
            "xml_name": "valueSource",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_tendency",
            "xml_name": "valueTendency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_state",
            "xml_name": "valueState",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:MeasurementListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class MeasurementListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:MeasurementValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTypeType"
        },
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


@spine_type('ns_p:MeasurementListDataType', is_value_type=False, no_attrib_name=False)
class MeasurementListDataType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_data",
            "xml_name": "measurementData",
            "type": "ns_p:MeasurementDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:MeasurementValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTypeType"
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_source",
            "xml_name": "valueSource",
            "type": "ns_p:MeasurementValueSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueSourceType"
        },
        {
            "name": "value_tendency",
            "xml_name": "valueTendency",
            "type": "ns_p:MeasurementValueTendencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueTendencyType"
        },
        {
            "name": "value_state",
            "xml_name": "valueState",
            "type": "ns_p:MeasurementValueStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementValueStateType"
        },
    ]


@spine_type('ns_p:MeasurementDataElementsType', is_value_type=False, no_attrib_name=False)
class MeasurementDataElementsType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
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
            "name": "value_source",
            "xml_name": "valueSource",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_tendency",
            "xml_name": "valueTendency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_state",
            "xml_name": "valueState",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

