# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import AbsoluteOrRecurringTimeElementsType
    from spine.base_type.commondatatypes import AbsoluteOrRecurringTimeType
    from spine.base_type.commondatatypes import DaysOfWeekType
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import RecurrenceInformationElementsType
    from spine.base_type.commondatatypes import RecurrenceInformationType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.base_type.commondatatypes import TimePeriodElementsType
    from spine.base_type.commondatatypes import TimePeriodType
    from spine.base_type.tariffinformation import IncentiveDataElementsType
    from spine.base_type.tariffinformation import IncentiveDataType
    from spine.base_type.tariffinformation import IncentiveDescriptionDataElementsType
    from spine.base_type.tariffinformation import IncentiveDescriptionDataType
    from spine.base_type.tariffinformation import TariffDataElementsType
    from spine.base_type.tariffinformation import TariffDataType
    from spine.base_type.tariffinformation import TariffDescriptionDataElementsType
    from spine.base_type.tariffinformation import TariffDescriptionDataType
    from spine.base_type.tariffinformation import TariffOverallConstraintsDataElementsType
    from spine.base_type.tariffinformation import TariffOverallConstraintsDataType
    from spine.base_type.tariffinformation import TierBoundaryDataElementsType
    from spine.base_type.tariffinformation import TierBoundaryDataType
    from spine.base_type.tariffinformation import TierBoundaryDescriptionDataElementsType
    from spine.base_type.tariffinformation import TierBoundaryDescriptionDataType
    from spine.base_type.tariffinformation import TierDataElementsType
    from spine.base_type.tariffinformation import TierDataType
    from spine.base_type.tariffinformation import TierDescriptionDataElementsType
    from spine.base_type.tariffinformation import TierDescriptionDataType
    from spine.base_type.timetable import TimeTableConstraintsDataElementsType
    from spine.base_type.timetable import TimeTableConstraintsDataType
    from spine.base_type.timetable import TimeTableDataElementsType
    from spine.base_type.timetable import TimeTableDataType
    from spine.enums.commondatatypes import MonthType
    from spine.simple_type.commondatatypes import CalendarWeekType
    from spine.simple_type.commondatatypes import DayOfMonthType
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
    from spine.simple_type.timetable import TimeSlotCountType
    from spine.simple_type.timetable import TimeSlotIdType
    from spine.simple_type.timetable import TimeTableIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import OccurrenceType
    from spine.union_type.commondatatypes import RecurringIntervalType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.tariffinformation import IncentiveTypeType
    from spine.union_type.tariffinformation import IncentiveValueTypeType
    from spine.union_type.tariffinformation import TierBoundaryTypeType
    from spine.union_type.tariffinformation import TierTypeType



@spine_type('ns_p:Anonymous_4503067984', is_value_type=False, no_attrib_name=False)
class Anonymous_4503067984(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503067984 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503067104', is_value_type=False, no_attrib_name=False)
class Anonymous_4503067104(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503067104 -> ComplexType
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


@spine_type('ns_p:IncentiveTableTierElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableTierElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableTierElementsType -> ComplexType
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
            "name": "boundary_id",
            "xml_name": "boundaryId",
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
            "name": "upper_boundary_value",
            "xml_name": "upperBoundaryValue",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
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


@spine_type('ns_p:Anonymous_4503064640', is_value_type=False, no_attrib_name=False)
class Anonymous_4503064640(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503064640 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "date_time",
            "xml_name": "dateTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "month",
            "xml_name": "month",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_month",
            "xml_name": "dayOfMonth",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_week_occurrence",
            "xml_name": "dayOfWeekOccurrence",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "days_of_week",
            "xml_name": "daysOfWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time",
            "xml_name": "time",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "relative",
            "xml_name": "relative",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503051248', is_value_type=False, no_attrib_name=False)
class Anonymous_4503051248(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503051248 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "date_time",
            "xml_name": "dateTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "month",
            "xml_name": "month",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_month",
            "xml_name": "dayOfMonth",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_week_occurrence",
            "xml_name": "dayOfWeekOccurrence",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "days_of_week",
            "xml_name": "daysOfWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time",
            "xml_name": "time",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "relative",
            "xml_name": "relative",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503038080', is_value_type=False, no_attrib_name=False)
class Anonymous_4503038080(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503038080 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503037200', is_value_type=False, no_attrib_name=False)
class Anonymous_4503037200(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503037200 -> ComplexType
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


@spine_type('ns_p:IncentiveTableTierType', is_value_type=False, no_attrib_name=False)
class IncentiveTableTierType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableTierType -> ComplexType
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
            "name": "boundary_id",
            "xml_name": "boundaryId",
            "type": "ns_p:TierBoundaryIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryIdType"
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
        {
            "name": "incentive_id",
            "xml_name": "incentiveId",
            "type": "ns_p:IncentiveIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveIdType"
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


@spine_type('ns_p:Anonymous_4503025792', is_value_type=False, no_attrib_name=False)
class Anonymous_4503025792(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503025792 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "date_time",
            "xml_name": "dateTime",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "month",
            "xml_name": "month",
            "type": "ns_p:MonthType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MonthType"
        },
        {
            "name": "day_of_month",
            "xml_name": "dayOfMonth",
            "type": "ns_p:DayOfMonthType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DayOfMonthType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:CalendarWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CalendarWeekType"
        },
        {
            "name": "day_of_week_occurrence",
            "xml_name": "dayOfWeekOccurrence",
            "type": "ns_p:OccurrenceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OccurrenceType"
        },
        {
            "name": "days_of_week",
            "xml_name": "daysOfWeek",
            "type": "ns_p:DaysOfWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DaysOfWeekType"
        },
        {
            "name": "monday",
            "xml_name": "monday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "tuesday",
            "xml_name": "tuesday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "wednesday",
            "xml_name": "wednesday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "thursday",
            "xml_name": "thursday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "friday",
            "xml_name": "friday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "saturday",
            "xml_name": "saturday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "sunday",
            "xml_name": "sunday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time",
            "xml_name": "time",
            "type": "xs:time",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "relative",
            "xml_name": "relative",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4503024736', is_value_type=False, no_attrib_name=False)
class Anonymous_4503024736(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503024736 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "date_time",
            "xml_name": "dateTime",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "month",
            "xml_name": "month",
            "type": "ns_p:MonthType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MonthType"
        },
        {
            "name": "day_of_month",
            "xml_name": "dayOfMonth",
            "type": "ns_p:DayOfMonthType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DayOfMonthType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:CalendarWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CalendarWeekType"
        },
        {
            "name": "day_of_week_occurrence",
            "xml_name": "dayOfWeekOccurrence",
            "type": "ns_p:OccurrenceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OccurrenceType"
        },
        {
            "name": "days_of_week",
            "xml_name": "daysOfWeek",
            "type": "ns_p:DaysOfWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DaysOfWeekType"
        },
        {
            "name": "monday",
            "xml_name": "monday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "tuesday",
            "xml_name": "tuesday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "wednesday",
            "xml_name": "wednesday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "thursday",
            "xml_name": "thursday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "friday",
            "xml_name": "friday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "saturday",
            "xml_name": "saturday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "sunday",
            "xml_name": "sunday",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time",
            "xml_name": "time",
            "type": "xs:time",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "relative",
            "xml_name": "relative",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4503149552', is_value_type=False, no_attrib_name=False)
class Anonymous_4503149552(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503149552 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503148672', is_value_type=False, no_attrib_name=False)
class Anonymous_4503148672(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503148672 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503147616', is_value_type=False, no_attrib_name=False)
class Anonymous_4503147616(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503147616 -> ComplexType
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


@spine_type('ns_p:IncentiveTableDescriptionTierElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionTierElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionTierElementsType -> ComplexType
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
    ]


@spine_type('ns_p:Anonymous_4503113968', is_value_type=False, no_attrib_name=False)
class Anonymous_4503113968(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503113968 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503104848', is_value_type=False, no_attrib_name=False)
class Anonymous_4503104848(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503104848 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503103792', is_value_type=False, no_attrib_name=False)
class Anonymous_4503103792(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503103792 -> ComplexType
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


@spine_type('ns_p:IncentiveTableDescriptionTierType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionTierType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionTierType -> ComplexType
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
    ]


@spine_type('ns_p:Anonymous_4503050016', is_value_type=False, no_attrib_name=False)
class Anonymous_4503050016(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503050016 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_slot_id",
            "xml_name": "timeSlotId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "recurrence_information",
            "xml_name": "recurrenceInformation",
            "type": "ns_p:RecurrenceInformationElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "RecurrenceInformationElementsType"
        },
        {
            "name": "recurring_interval",
            "xml_name": "recurringInterval",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "recurring_interval_step",
            "xml_name": "recurringIntervalStep",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "first_execution",
            "xml_name": "firstExecution",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "execution_count",
            "xml_name": "executionCount",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "last_execution",
            "xml_name": "lastExecution",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:AbsoluteOrRecurringTimeElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeElementsType"
        },
        {
            "name": "date_time",
            "xml_name": "dateTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "month",
            "xml_name": "month",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_month",
            "xml_name": "dayOfMonth",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_week_occurrence",
            "xml_name": "dayOfWeekOccurrence",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "days_of_week",
            "xml_name": "daysOfWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time",
            "xml_name": "time",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "relative",
            "xml_name": "relative",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:AbsoluteOrRecurringTimeElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeElementsType"
        },
    ]


@spine_type('ns_p:IncentiveTableIncentiveSlotElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableIncentiveSlotElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableIncentiveSlotElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_slot_id",
            "xml_name": "timeSlotId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:Anonymous_4503051248",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503051248"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:Anonymous_4503064640",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503064640"
        },
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableTierElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableTierElementsType"
        },
        {
            "name": "boundary",
            "xml_name": "boundary",
            "type": "ns_p:Anonymous_4503067104",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503067104"
        },
        {
            "name": "incentive",
            "xml_name": "incentive",
            "type": "ns_p:Anonymous_4503067984",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503067984"
        },
    ]


@spine_type('ns_p:Anonymous_4503010992', is_value_type=False, no_attrib_name=False)
class Anonymous_4503010992(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503010992 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "time_slot_id",
            "xml_name": "timeSlotId",
            "type": "ns_p:TimeSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotIdType"
        },
        {
            "name": "recurrence_information",
            "xml_name": "recurrenceInformation",
            "type": "ns_p:RecurrenceInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "RecurrenceInformationType"
        },
        {
            "name": "recurring_interval",
            "xml_name": "recurringInterval",
            "type": "ns_p:RecurringIntervalType",
            "is_array": False,
            "is_optional": True,
            "class_check": "RecurringIntervalType"
        },
        {
            "name": "recurring_interval_step",
            "xml_name": "recurringIntervalStep",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "first_execution",
            "xml_name": "firstExecution",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "execution_count",
            "xml_name": "executionCount",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "last_execution",
            "xml_name": "lastExecution",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:AbsoluteOrRecurringTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeType"
        },
        {
            "name": "date_time",
            "xml_name": "dateTime",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "month",
            "xml_name": "month",
            "type": "ns_p:MonthType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MonthType"
        },
        {
            "name": "day_of_month",
            "xml_name": "dayOfMonth",
            "type": "ns_p:DayOfMonthType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DayOfMonthType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:CalendarWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CalendarWeekType"
        },
        {
            "name": "day_of_week_occurrence",
            "xml_name": "dayOfWeekOccurrence",
            "type": "ns_p:OccurrenceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OccurrenceType"
        },
        {
            "name": "days_of_week",
            "xml_name": "daysOfWeek",
            "type": "ns_p:DaysOfWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DaysOfWeekType"
        },
        {
            "name": "time",
            "xml_name": "time",
            "type": "xs:time",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "relative",
            "xml_name": "relative",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:AbsoluteOrRecurringTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeType"
        },
    ]


@spine_type('ns_p:IncentiveTableIncentiveSlotType', is_value_type=False, no_attrib_name=False)
class IncentiveTableIncentiveSlotType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableIncentiveSlotType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_slot_id",
            "xml_name": "timeSlotId",
            "type": "ns_p:TimeSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotIdType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:Anonymous_4503024736",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503024736"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:Anonymous_4503025792",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503025792"
        },
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableTierType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "boundary",
            "xml_name": "boundary",
            "type": "ns_p:Anonymous_4503037200",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "incentive",
            "xml_name": "incentive",
            "type": "ns_p:Anonymous_4503038080",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:Anonymous_4503194256', is_value_type=False, no_attrib_name=False)
class Anonymous_4503194256(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503194256 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_count_min",
            "xml_name": "slotCountMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_count_max",
            "xml_name": "slotCountMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_duration_min",
            "xml_name": "slotDurationMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_duration_max",
            "xml_name": "slotDurationMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_duration_step_size",
            "xml_name": "slotDurationStepSize",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_shift_step_size",
            "xml_name": "slotShiftStepSize",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "first_slot_begins_at",
            "xml_name": "firstSlotBeginsAt",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503193376', is_value_type=False, no_attrib_name=False)
class Anonymous_4503193376(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503193376 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503192320', is_value_type=False, no_attrib_name=False)
class Anonymous_4503192320(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503192320 -> ComplexType
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


@spine_type('ns_p:IncentiveTableConstraintsElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableConstraintsElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsElementsType -> ComplexType
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
        {
            "name": "slot_count_max",
            "xml_name": "slotCountMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503181440', is_value_type=False, no_attrib_name=False)
class Anonymous_4503181440(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503181440 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "slot_count_min",
            "xml_name": "slotCountMin",
            "type": "ns_p:TimeSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotCountType"
        },
        {
            "name": "slot_count_max",
            "xml_name": "slotCountMax",
            "type": "ns_p:TimeSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotCountType"
        },
        {
            "name": "slot_duration_min",
            "xml_name": "slotDurationMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "slot_duration_max",
            "xml_name": "slotDurationMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "slot_duration_step_size",
            "xml_name": "slotDurationStepSize",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "slot_shift_step_size",
            "xml_name": "slotShiftStepSize",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "first_slot_begins_at",
            "xml_name": "firstSlotBeginsAt",
            "type": "xs:time",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4503180560', is_value_type=False, no_attrib_name=False)
class Anonymous_4503180560(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503180560 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503179504', is_value_type=False, no_attrib_name=False)
class Anonymous_4503179504(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503179504 -> ComplexType
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


@spine_type('ns_p:IncentiveTableConstraintsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableConstraintsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsType -> ComplexType
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
        {
            "name": "slot_count_max",
            "xml_name": "slotCountMax",
            "type": "ns_p:TimeSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotCountType"
        },
    ]


@spine_type('ns_p:Anonymous_4503132816', is_value_type=False, no_attrib_name=False)
class Anonymous_4503132816(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503132816 -> ComplexType
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


@spine_type('ns_p:IncentiveTableDescriptionElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionElementsType -> ComplexType
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
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableDescriptionTierElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDescriptionTierElementsType"
        },
        {
            "name": "tier_description",
            "xml_name": "tierDescription",
            "type": "ns_p:Anonymous_4503147616",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503147616"
        },
        {
            "name": "boundary_description",
            "xml_name": "boundaryDescription",
            "type": "ns_p:Anonymous_4503148672",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503148672"
        },
        {
            "name": "incentive_description",
            "xml_name": "incentiveDescription",
            "type": "ns_p:Anonymous_4503149552",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503149552"
        },
    ]


@spine_type('ns_p:Anonymous_4503079392', is_value_type=False, no_attrib_name=False)
class Anonymous_4503079392(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503079392 -> ComplexType
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


@spine_type('ns_p:IncentiveTableDescriptionType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionType -> ComplexType
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
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableDescriptionTierType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tier_description",
            "xml_name": "tierDescription",
            "type": "ns_p:Anonymous_4503103792",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503103792"
        },
        {
            "name": "boundary_description",
            "xml_name": "boundaryDescription",
            "type": "ns_p:Anonymous_4503104848",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "incentive_description",
            "xml_name": "incentiveDescription",
            "type": "ns_p:Anonymous_4503113968",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:Anonymous_4503048784', is_value_type=False, no_attrib_name=False)
class Anonymous_4503048784(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503048784 -> ComplexType
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


@spine_type('ns_p:IncentiveTableElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableElementsType -> ComplexType
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
            "name": "incentive_slot",
            "xml_name": "incentiveSlot",
            "type": "ns_p:IncentiveTableIncentiveSlotElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableIncentiveSlotElementsType"
        },
        {
            "name": "time_interval",
            "xml_name": "timeInterval",
            "type": "ns_p:Anonymous_4503050016",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503050016"
        },
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableTierElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableTierElementsType"
        },
    ]


@spine_type('ns_p:Anonymous_4503009584', is_value_type=False, no_attrib_name=False)
class Anonymous_4503009584(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503009584 -> ComplexType
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


@spine_type('ns_p:IncentiveTableType', is_value_type=False, no_attrib_name=False)
class IncentiveTableType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableType -> ComplexType
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
            "name": "incentive_slot",
            "xml_name": "incentiveSlot",
            "type": "ns_p:IncentiveTableIncentiveSlotType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "time_interval",
            "xml_name": "timeInterval",
            "type": "ns_p:Anonymous_4503010992",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503010992"
        },
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableTierType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:IncentiveTableConstraintsDataSelectorsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableConstraintsDataSelectorsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
    ]


@spine_type('ns_p:IncentiveTableConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_table_constraints",
            "xml_name": "incentiveTableConstraints",
            "type": "ns_p:IncentiveTableConstraintsElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableConstraintsElementsType"
        },
        {
            "name": "tariff",
            "xml_name": "tariff",
            "type": "ns_p:Anonymous_4503192320",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503192320"
        },
        {
            "name": "tariff_constraints",
            "xml_name": "tariffConstraints",
            "type": "ns_p:Anonymous_4503193376",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503193376"
        },
        {
            "name": "incentive_slot_constraints",
            "xml_name": "incentiveSlotConstraints",
            "type": "ns_p:Anonymous_4503194256",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503194256"
        },
    ]


@spine_type('ns_p:IncentiveTableConstraintsDataType', is_value_type=False, no_attrib_name=False)
class IncentiveTableConstraintsDataType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_table_constraints",
            "xml_name": "incentiveTableConstraints",
            "type": "ns_p:IncentiveTableConstraintsType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff",
            "xml_name": "tariff",
            "type": "ns_p:Anonymous_4503179504",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503179504"
        },
        {
            "name": "tariff_constraints",
            "xml_name": "tariffConstraints",
            "type": "ns_p:Anonymous_4503180560",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503180560"
        },
        {
            "name": "incentive_slot_constraints",
            "xml_name": "incentiveSlotConstraints",
            "type": "ns_p:Anonymous_4503181440",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503181440"
        },
    ]


@spine_type('ns_p:IncentiveTableDescriptionDataSelectorsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionDataSelectorsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionDataSelectorsType -> ComplexType
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
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
    ]


@spine_type('ns_p:IncentiveTableDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_table_description",
            "xml_name": "incentiveTableDescription",
            "type": "ns_p:IncentiveTableDescriptionElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDescriptionElementsType"
        },
        {
            "name": "tariff_description",
            "xml_name": "tariffDescription",
            "type": "ns_p:Anonymous_4503132816",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503132816"
        },
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableDescriptionTierElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDescriptionTierElementsType"
        },
    ]


@spine_type('ns_p:IncentiveTableDescriptionDataType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDescriptionDataType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_table_description",
            "xml_name": "incentiveTableDescription",
            "type": "ns_p:IncentiveTableDescriptionType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff_description",
            "xml_name": "tariffDescription",
            "type": "ns_p:Anonymous_4503079392",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503079392"
        },
        {
            "name": "tier",
            "xml_name": "tier",
            "type": "ns_p:IncentiveTableDescriptionTierType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:IncentiveTableDataSelectorsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDataSelectorsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "tariff_id",
            "xml_name": "tariffId",
            "type": "ns_p:TariffIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffIdType"
        },
    ]


@spine_type('ns_p:IncentiveTableDataElementsType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDataElementsType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_table",
            "xml_name": "incentiveTable",
            "type": "ns_p:IncentiveTableElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableElementsType"
        },
        {
            "name": "tariff",
            "xml_name": "tariff",
            "type": "ns_p:Anonymous_4503048784",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503048784"
        },
        {
            "name": "incentive_slot",
            "xml_name": "incentiveSlot",
            "type": "ns_p:IncentiveTableIncentiveSlotElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableIncentiveSlotElementsType"
        },
    ]


@spine_type('ns_p:Anonymous_4503066048', is_value_type=False, no_attrib_name=False)
class Anonymous_4503066048(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503066048 -> ComplexType
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


@spine_type('ns_p:IncentiveTableDataType', is_value_type=False, no_attrib_name=False)
class IncentiveTableDataType(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "incentive_table",
            "xml_name": "incentiveTable",
            "type": "ns_p:IncentiveTableType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "tariff",
            "xml_name": "tariff",
            "type": "ns_p:Anonymous_4503009584",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503009584"
        },
        {
            "name": "incentive_slot",
            "xml_name": "incentiveSlot",
            "type": "ns_p:IncentiveTableIncentiveSlotType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:Anonymous_4503036144', is_value_type=False, no_attrib_name=False)
class Anonymous_4503036144(SpineBase): # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:Anonymous_4503036144 -> ComplexType
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

