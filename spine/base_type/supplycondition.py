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
    from spine.simple_type.supplycondition import ConditionIdType
    from spine.simple_type.threshold import ThresholdIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CommodityTypeType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.supplycondition import GridConditionType
    from spine.union_type.supplycondition import SupplyConditionEventTypeType
    from spine.union_type.supplycondition import SupplyConditionOriginatorType



@spine_type('ns_p:SupplyConditionThresholdRelationDataType', is_value_type=False, no_attrib_name=False)
class SupplyConditionThresholdRelationDataType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionThresholdRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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


@spine_type('ns_p:SupplyConditionDescriptionDataType', is_value_type=False, no_attrib_name=False)
class SupplyConditionDescriptionDataType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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
            "name": "positive_energy_direction",
            "xml_name": "positiveEnergyDirection",
            "type": "ns_p:EnergyDirectionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyDirectionType"
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


@spine_type('ns_p:SupplyConditionDataType', is_value_type=False, no_attrib_name=False)
class SupplyConditionDataType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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
            "name": "event_type",
            "xml_name": "eventType",
            "type": "ns_p:SupplyConditionEventTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionEventTypeType"
        },
        {
            "name": "originator",
            "xml_name": "originator",
            "type": "ns_p:SupplyConditionOriginatorType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionOriginatorType"
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
            "name": "threshold_percentage",
            "xml_name": "thresholdPercentage",
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
            "name": "relevant_period",
            "xml_name": "relevantPeriod",
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
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
        {
            "name": "grid_condition",
            "xml_name": "gridCondition",
            "type": "ns_p:GridConditionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "GridConditionType"
        },
    ]


@spine_type('ns_p:SupplyConditionThresholdRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SupplyConditionThresholdRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionThresholdRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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


@spine_type('ns_p:SupplyConditionThresholdRelationListDataType', is_value_type=False, no_attrib_name=False)
class SupplyConditionThresholdRelationListDataType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionThresholdRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "supply_condition_threshold_relation_data",
            "xml_name": "supplyConditionThresholdRelationData",
            "type": "ns_p:SupplyConditionThresholdRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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


@spine_type('ns_p:SupplyConditionThresholdRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class SupplyConditionThresholdRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionThresholdRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
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


@spine_type('ns_p:SupplyConditionDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SupplyConditionDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
        },
    ]


@spine_type('ns_p:SupplyConditionDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class SupplyConditionDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "supply_condition_description_data",
            "xml_name": "supplyConditionDescriptionData",
            "type": "ns_p:SupplyConditionDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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
            "name": "positive_energy_direction",
            "xml_name": "positiveEnergyDirection",
            "type": "ns_p:EnergyDirectionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyDirectionType"
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


@spine_type('ns_p:SupplyConditionDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class SupplyConditionDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
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
            "name": "positive_energy_direction",
            "xml_name": "positiveEnergyDirection",
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


@spine_type('ns_p:SupplyConditionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SupplyConditionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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
        {
            "name": "event_type",
            "xml_name": "eventType",
            "type": "ns_p:SupplyConditionEventTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionEventTypeType"
        },
        {
            "name": "originator",
            "xml_name": "originator",
            "type": "ns_p:SupplyConditionOriginatorType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionOriginatorType"
        },
    ]


@spine_type('ns_p:SupplyConditionListDataType', is_value_type=False, no_attrib_name=False)
class SupplyConditionListDataType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "supply_condition_data",
            "xml_name": "supplyConditionData",
            "type": "ns_p:SupplyConditionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "condition_id",
            "xml_name": "conditionId",
            "type": "ns_p:ConditionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ConditionIdType"
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
            "name": "event_type",
            "xml_name": "eventType",
            "type": "ns_p:SupplyConditionEventTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionEventTypeType"
        },
        {
            "name": "originator",
            "xml_name": "originator",
            "type": "ns_p:SupplyConditionOriginatorType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionOriginatorType"
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
            "name": "threshold_percentage",
            "xml_name": "thresholdPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "relevant_period",
            "xml_name": "relevantPeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
        {
            "name": "grid_condition",
            "xml_name": "gridCondition",
            "type": "ns_p:GridConditionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "GridConditionType"
        },
    ]


@spine_type('ns_p:SupplyConditionDataElementsType', is_value_type=False, no_attrib_name=False)
class SupplyConditionDataElementsType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "condition_id",
            "xml_name": "conditionId",
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
            "name": "event_type",
            "xml_name": "eventType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "originator",
            "xml_name": "originator",
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
            "name": "threshold_percentage",
            "xml_name": "thresholdPercentage",
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
            "name": "relevant_period",
            "xml_name": "relevantPeriod",
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
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "grid_condition",
            "xml_name": "gridCondition",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

