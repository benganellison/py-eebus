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
    from spine.simple_type.tariffinformation import CommodityIdType
    from spine.simple_type.tariffinformation import IncentiveCountType
    from spine.simple_type.tariffinformation import IncentiveIdType
    from spine.simple_type.tariffinformation import IncentivePriorityType
    from spine.simple_type.tariffinformation import TariffCountType
    from spine.simple_type.tariffinformation import TariffIdType
    from spine.simple_type.tariffinformation import TierBoundaryCountType
    from spine.simple_type.tariffinformation import TierBoundaryIdType
    from spine.simple_type.tariffinformation import TierCountType
    from spine.simple_type.tariffinformation import TierIdType
    from spine.simple_type.timetable import TimeTableIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CommodityTypeType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.tariffinformation import IncentiveTypeType
    from spine.union_type.tariffinformation import IncentiveValueTypeType
    from spine.union_type.tariffinformation import TierBoundaryTypeType
    from spine.union_type.tariffinformation import TierTypeType



@spine_type('ns_p:IncentiveDescriptionDataType', is_value_type=False, no_attrib_name=False)
class IncentiveDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
        {
            "name": "incentive_type",
            "xml_name": "incentiveType",
            "type": "ns_p:IncentiveTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTypeType"
        },
        {
            "name": "incentive_priority",
            "xml_name": "incentivePriority",
            "type": "ns_p:IncentivePriorityType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentivePriorityType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
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


@spine_type('ns_p:IncentiveDataType', is_value_type=False, no_attrib_name=False)
class IncentiveDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:IncentiveValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveValueTypeType"
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
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


@spine_type('ns_p:TierDescriptionDataType', is_value_type=False, no_attrib_name=False)
class TierDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "tier_type",
            "xml_name": "tierType",
            "type": "ns_p:TierTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierTypeType"
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


@spine_type('ns_p:TierIncentiveRelationDataType', is_value_type=False, no_attrib_name=False)
class TierIncentiveRelationDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierIncentiveRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TierDataType', is_value_type=False, no_attrib_name=False)
class TierDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "active_incentive_id",
            "xml_name": "activeIncentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:CommodityDataType', is_value_type=False, no_attrib_name=False)
class CommodityDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:CommodityDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
            "type": "ns_p:CommodityIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityIdType"
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


@spine_type('ns_p:TierBoundaryDescriptionDataType', is_value_type=False, no_attrib_name=False)
class TierBoundaryDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
        },
        {
            "name": "boundary_type",
            "xml_name": "boundaryType",
            "type": "ns_p:TierBoundaryTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryTypeType"
        },
        {
            "name": "valid_for_tier_id",
            "xml_name": "validForTierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "switch_to_tier_id_when_lower",
            "xml_name": "switchToTierIdWhenLower",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "switch_to_tier_id_when_higher",
            "xml_name": "switchToTierIdWhenHigher",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "boundary_unit",
            "xml_name": "boundaryUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
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


@spine_type('ns_p:TierBoundaryDataType', is_value_type=False, no_attrib_name=False)
class TierBoundaryDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "lower_boundary_value",
            "xml_name": "lowerBoundaryValue",
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
            "name": "upper_boundary_value",
            "xml_name": "upperBoundaryValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TariffDescriptionDataType', is_value_type=False, no_attrib_name=False)
class TariffDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
            "type": "ns_p:CommodityIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityIdType"
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
            "name": "tariff_writeable",
            "xml_name": "tariffWriteable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "update_required",
            "xml_name": "updateRequired",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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
        {
            "name": "slot_id_support",
            "xml_name": "slotIdSupport",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:TariffBoundaryRelationDataType', is_value_type=False, no_attrib_name=False)
class TariffBoundaryRelationDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffBoundaryRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TariffTierRelationDataType', is_value_type=False, no_attrib_name=False)
class TariffTierRelationDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffTierRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TariffDataType', is_value_type=False, no_attrib_name=False)
class TariffDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "active_tier_id",
            "xml_name": "activeTierId",
            "type": "ns_p:TierIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:IncentiveDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class IncentiveDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
        {
            "name": "incentive_type",
            "xml_name": "incentiveType",
            "type": "ns_p:IncentiveTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTypeType"
        },
    ]


@spine_type('ns_p:IncentiveDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class IncentiveDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_description_data",
            "xml_name": "incentiveDescriptionData",
            "type": "ns_p:IncentiveDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
        {
            "name": "incentive_type",
            "xml_name": "incentiveType",
            "type": "ns_p:IncentiveTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTypeType"
        },
        {
            "name": "incentive_priority",
            "xml_name": "incentivePriority",
            "type": "ns_p:IncentivePriorityType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentivePriorityType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
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


@spine_type('ns_p:IncentiveListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class IncentiveListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:IncentiveValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveValueTypeType"
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


@spine_type('ns_p:IncentiveListDataType', is_value_type=False, no_attrib_name=False)
class IncentiveListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_data",
            "xml_name": "incentiveData",
            "type": "ns_p:IncentiveDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:IncentiveValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveValueTypeType"
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
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
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
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TierDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TierDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "tier_type",
            "xml_name": "tierType",
            "type": "ns_p:TierTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierTypeType"
        },
    ]


@spine_type('ns_p:TierDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class TierDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_description_data",
            "xml_name": "tierDescriptionData",
            "type": "ns_p:TierDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "tier_type",
            "xml_name": "tierType",
            "type": "ns_p:TierTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierTypeType"
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


@spine_type('ns_p:TierIncentiveRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TierIncentiveRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierIncentiveRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
    ]


@spine_type('ns_p:TierIncentiveRelationListDataType', is_value_type=False, no_attrib_name=False)
class TierIncentiveRelationListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierIncentiveRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_incentive_relation_data",
            "xml_name": "tierIncentiveRelationData",
            "type": "ns_p:TierIncentiveRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TierIncentiveRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class TierIncentiveRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierIncentiveRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TierListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TierListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "active_incentive_id",
            "xml_name": "activeIncentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
        },
    ]


@spine_type('ns_p:TierListDataType', is_value_type=False, no_attrib_name=False)
class TierListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_data",
            "xml_name": "tierData",
            "type": "ns_p:TierDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "active_incentive_id",
            "xml_name": "activeIncentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:CommodityListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class CommodityListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:CommodityListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
            "type": "ns_p:CommodityIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityIdType"
        },
        {
            "name": "commodity_type",
            "xml_name": "commodityType",
            "type": "ns_p:CommodityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityTypeType"
        },
    ]


@spine_type('ns_p:CommodityListDataType', is_value_type=False, no_attrib_name=False)
class CommodityListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:CommodityListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "commodity_data",
            "xml_name": "commodityData",
            "type": "ns_p:CommodityDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
            "type": "ns_p:CommodityIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityIdType"
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


@spine_type('ns_p:CommodityDataElementsType', is_value_type=False, no_attrib_name=False)
class CommodityDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:CommodityDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
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


@spine_type('ns_p:TierBoundaryDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TierBoundaryDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
        },
        {
            "name": "boundary_type",
            "xml_name": "boundaryType",
            "type": "ns_p:TierBoundaryTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryTypeType"
        },
    ]


@spine_type('ns_p:TierBoundaryDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class TierBoundaryDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_boundary_description_data",
            "xml_name": "tierBoundaryDescriptionData",
            "type": "ns_p:TierBoundaryDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
        },
        {
            "name": "boundary_type",
            "xml_name": "boundaryType",
            "type": "ns_p:TierBoundaryTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryTypeType"
        },
        {
            "name": "valid_for_tier_id",
            "xml_name": "validForTierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "switch_to_tier_id_when_lower",
            "xml_name": "switchToTierIdWhenLower",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "switch_to_tier_id_when_higher",
            "xml_name": "switchToTierIdWhenHigher",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
        {
            "name": "boundary_unit",
            "xml_name": "boundaryUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
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


@spine_type('ns_p:TierBoundaryListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TierBoundaryListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
        },
    ]


@spine_type('ns_p:TierBoundaryListDataType', is_value_type=False, no_attrib_name=False)
class TierBoundaryListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_boundary_data",
            "xml_name": "tierBoundaryData",
            "type": "ns_p:TierBoundaryDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "lower_boundary_value",
            "xml_name": "lowerBoundaryValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "upper_boundary_value",
            "xml_name": "upperBoundaryValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TariffDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TariffDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
            "type": "ns_p:CommodityIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityIdType"
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


@spine_type('ns_p:TariffDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class TariffDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_description_data",
            "xml_name": "tariffDescriptionData",
            "type": "ns_p:TariffDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
            "type": "ns_p:CommodityIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityIdType"
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
            "name": "tariff_writeable",
            "xml_name": "tariffWriteable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "update_required",
            "xml_name": "updateRequired",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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
        {
            "name": "slot_id_support",
            "xml_name": "slotIdSupport",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:TariffBoundaryRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TariffBoundaryRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffBoundaryRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
        },
    ]


@spine_type('ns_p:TariffBoundaryRelationListDataType', is_value_type=False, no_attrib_name=False)
class TariffBoundaryRelationListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffBoundaryRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_boundary_relation_data",
            "xml_name": "tariffBoundaryRelationData",
            "type": "ns_p:TariffBoundaryRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TariffBoundaryRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class TariffBoundaryRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffBoundaryRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TariffTierRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TariffTierRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffTierRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
    ]


@spine_type('ns_p:TariffTierRelationListDataType', is_value_type=False, no_attrib_name=False)
class TariffTierRelationListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffTierRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_tier_relation_data",
            "xml_name": "tariffTierRelationData",
            "type": "ns_p:TariffTierRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:TierIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TariffTierRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class TariffTierRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffTierRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TariffListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TariffListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "active_tier_id",
            "xml_name": "activeTierId",
            "type": "ns_p:TierIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIdType"
        },
    ]


@spine_type('ns_p:TariffListDataType', is_value_type=False, no_attrib_name=False)
class TariffListDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_data",
            "xml_name": "tariffData",
            "type": "ns_p:TariffDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
        {
            "name": "active_tier_id",
            "xml_name": "activeTierId",
            "type": "ns_p:TierIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TariffOverallConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class TariffOverallConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffOverallConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "max_tariff_count",
            "xml_name": "maxTariffCount",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_boundary_count",
            "xml_name": "maxBoundaryCount",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_tier_count",
            "xml_name": "maxTierCount",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_incentive_count",
            "xml_name": "maxIncentiveCount",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_boundaries_per_tariff",
            "xml_name": "maxBoundariesPerTariff",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_tiers_per_tariff",
            "xml_name": "maxTiersPerTariff",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_boundaries_per_tier",
            "xml_name": "maxBoundariesPerTier",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_incentives_per_tier",
            "xml_name": "maxIncentivesPerTier",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TariffOverallConstraintsDataType', is_value_type=False, no_attrib_name=False)
class TariffOverallConstraintsDataType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffOverallConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "max_tariff_count",
            "xml_name": "maxTariffCount",
            "type": "ns_p:TariffCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffCountType"
        },
        {
            "name": "max_boundary_count",
            "xml_name": "maxBoundaryCount",
            "type": "ns_p:TierBoundaryCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryCountType"
        },
        {
            "name": "max_tier_count",
            "xml_name": "maxTierCount",
            "type": "ns_p:TierCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierCountType"
        },
        {
            "name": "max_incentive_count",
            "xml_name": "maxIncentiveCount",
            "type": "ns_p:IncentiveCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveCountType"
        },
        {
            "name": "max_boundaries_per_tariff",
            "xml_name": "maxBoundariesPerTariff",
            "type": "ns_p:TierBoundaryCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryCountType"
        },
        {
            "name": "max_tiers_per_tariff",
            "xml_name": "maxTiersPerTariff",
            "type": "ns_p:TierCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierCountType"
        },
        {
            "name": "max_boundaries_per_tier",
            "xml_name": "maxBoundariesPerTier",
            "type": "ns_p:TierBoundaryCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryCountType"
        },
        {
            "name": "max_incentives_per_tier",
            "xml_name": "maxIncentivesPerTier",
            "type": "ns_p:IncentiveCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveCountType"
        },
    ]


@spine_type('ns_p:TariffDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class TariffDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "commodity_id",
            "xml_name": "commodityId",
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
            "name": "tariff_writeable",
            "xml_name": "tariffWriteable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "update_required",
            "xml_name": "updateRequired",
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
        {
            "name": "slot_id_support",
            "xml_name": "slotIdSupport",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:IncentiveDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "incentive_type",
            "xml_name": "incentiveType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "incentive_priority",
            "xml_name": "incentivePriority",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
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


@spine_type('ns_p:TierBoundaryDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class TierBoundaryDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "boundary_type",
            "xml_name": "boundaryType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "valid_for_tier_id",
            "xml_name": "validForTierId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "switch_to_tier_id_when_lower",
            "xml_name": "switchToTierIdWhenLower",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "switch_to_tier_id_when_higher",
            "xml_name": "switchToTierIdWhenHigher",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "boundary_unit",
            "xml_name": "boundaryUnit",
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


@spine_type('ns_p:TierDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class TierDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "tier_type",
            "xml_name": "tierType",
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


@spine_type('ns_p:TariffDataElementsType', is_value_type=False, no_attrib_name=False)
class TariffDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TariffDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_tier_id",
            "xml_name": "activeTierId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:IncentiveDataElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:IncentiveDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TierBoundaryDataElementsType', is_value_type=False, no_attrib_name=False)
class TierBoundaryDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierBoundaryDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boundary_id",
            "xml_name": "boundaryId",
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "lower_boundary_value",
            "xml_name": "lowerBoundaryValue",
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
            "name": "upper_boundary_value",
            "xml_name": "upperBoundaryValue",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:TierDataElementsType', is_value_type=False, no_attrib_name=False)
class TierDataElementsType(SpineBase): # EEBus_SPINE_TS_TariffInformation.xsd:ns_p:TierDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tier_id",
            "xml_name": "tierId",
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
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_incentive_id",
            "xml_name": "activeIncentiveId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

