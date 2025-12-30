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
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.base_type.commondatatypes import TimePeriodElementsType
    from spine.base_type.commondatatypes import TimePeriodType
    from spine.enums.commondatatypes import MonthType
    from spine.simple_type.commondatatypes import CalendarWeekType
    from spine.simple_type.commondatatypes import DayOfMonthType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.measurement import MeasurementIdType
    from spine.simple_type.timeseries import TimeSeriesIdType
    from spine.simple_type.timeseries import TimeSeriesSlotCountType
    from spine.simple_type.timeseries import TimeSeriesSlotIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import OccurrenceType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.timeseries import TimeSeriesTypeType



@spine_type('ns_p:TimeSeriesSlotType', is_value_type=False, no_attrib_name=False)
class TimeSeriesSlotType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesSlotType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_slot_id",
            "xml_name": "timeSeriesSlotId",
            "type": "ns_p:TimeSeriesSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotIdType"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "recurrence_information",
            "xml_name": "recurrenceInformation",
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
            "name": "min_value",
            "xml_name": "minValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "max_value",
            "xml_name": "maxValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TimeSeriesConstraintsDataType', is_value_type=False, no_attrib_name=False)
class TimeSeriesConstraintsDataType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
        {
            "name": "slot_count_min",
            "xml_name": "slotCountMin",
            "type": "ns_p:TimeSeriesSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotCountType"
        },
        {
            "name": "slot_count_max",
            "xml_name": "slotCountMax",
            "type": "ns_p:TimeSeriesSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotCountType"
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
            "name": "earliest_time_series_start_time",
            "xml_name": "earliestTimeSeriesStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "latest_time_series_end_time",
            "xml_name": "latestTimeSeriesEndTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "slot_value_min",
            "xml_name": "slotValueMin",
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
            "name": "slot_value_max",
            "xml_name": "slotValueMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "slot_value_step_size",
            "xml_name": "slotValueStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TimeSeriesDescriptionDataType', is_value_type=False, no_attrib_name=False)
class TimeSeriesDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
        {
            "name": "time_series_type",
            "xml_name": "timeSeriesType",
            "type": "ns_p:TimeSeriesTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesTypeType"
        },
        {
            "name": "time_series_writeable",
            "xml_name": "timeSeriesWriteable",
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
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
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
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
    ]


@spine_type('ns_p:TimeSeriesDataType', is_value_type=False, no_attrib_name=False)
class TimeSeriesDataType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
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
            "name": "time_series_slot",
            "xml_name": "timeSeriesSlot",
            "type": "ns_p:TimeSeriesSlotType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "time_series_slot_id",
            "xml_name": "timeSeriesSlotId",
            "type": "ns_p:TimeSeriesSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotIdType"
        },
        {
            "name": "duration",
            "xml_name": "duration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "recurrence_information",
            "xml_name": "recurrenceInformation",
            "type": "ns_p:AbsoluteOrRecurringTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeType"
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
            "name": "min_value",
            "xml_name": "minValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "max_value",
            "xml_name": "maxValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TimeSeriesSlotElementsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesSlotElementsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesSlotElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_slot_id",
            "xml_name": "timeSeriesSlotId",
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
            "name": "duration",
            "xml_name": "duration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "recurrence_information",
            "xml_name": "recurrenceInformation",
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
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "min_value",
            "xml_name": "minValue",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_value",
            "xml_name": "maxValue",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TimeSeriesConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
    ]


@spine_type('ns_p:TimeSeriesConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class TimeSeriesConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_constraints_data",
            "xml_name": "timeSeriesConstraintsData",
            "type": "ns_p:TimeSeriesConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
        {
            "name": "slot_count_min",
            "xml_name": "slotCountMin",
            "type": "ns_p:TimeSeriesSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotCountType"
        },
        {
            "name": "slot_count_max",
            "xml_name": "slotCountMax",
            "type": "ns_p:TimeSeriesSlotCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotCountType"
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
            "name": "earliest_time_series_start_time",
            "xml_name": "earliestTimeSeriesStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "latest_time_series_end_time",
            "xml_name": "latestTimeSeriesEndTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "slot_value_min",
            "xml_name": "slotValueMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "slot_value_max",
            "xml_name": "slotValueMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "slot_value_step_size",
            "xml_name": "slotValueStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:TimeSeriesConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
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
            "name": "earliest_time_series_start_time",
            "xml_name": "earliestTimeSeriesStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "latest_time_series_end_time",
            "xml_name": "latestTimeSeriesEndTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_value_min",
            "xml_name": "slotValueMin",
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
            "name": "slot_value_max",
            "xml_name": "slotValueMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "slot_value_step_size",
            "xml_name": "slotValueStepSize",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:TimeSeriesDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
        {
            "name": "time_series_type",
            "xml_name": "timeSeriesType",
            "type": "ns_p:TimeSeriesTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesTypeType"
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


@spine_type('ns_p:TimeSeriesDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class TimeSeriesDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_description_data",
            "xml_name": "timeSeriesDescriptionData",
            "type": "ns_p:TimeSeriesDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
        {
            "name": "time_series_type",
            "xml_name": "timeSeriesType",
            "type": "ns_p:TimeSeriesTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesTypeType"
        },
        {
            "name": "time_series_writeable",
            "xml_name": "timeSeriesWriteable",
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
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
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
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
    ]


@spine_type('ns_p:TimeSeriesDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_series_type",
            "xml_name": "timeSeriesType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_series_writeable",
            "xml_name": "timeSeriesWriteable",
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
            "name": "measurement_id",
            "xml_name": "measurementId",
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
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TimeSeriesListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
        },
        {
            "name": "time_series_slot_id",
            "xml_name": "timeSeriesSlotId",
            "type": "ns_p:TimeSeriesSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotIdType"
        },
    ]


@spine_type('ns_p:TimeSeriesListDataType', is_value_type=False, no_attrib_name=False)
class TimeSeriesListDataType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_data",
            "xml_name": "timeSeriesData",
            "type": "ns_p:TimeSeriesDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
            "type": "ns_p:TimeSeriesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesIdType"
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
            "name": "time_series_slot",
            "xml_name": "timeSeriesSlot",
            "type": "ns_p:TimeSeriesSlotType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:TimeSeriesDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeSeriesDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_series_id",
            "xml_name": "timeSeriesId",
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
            "name": "time_series_slot",
            "xml_name": "timeSeriesSlot",
            "type": "ns_p:TimeSeriesSlotElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotElementsType"
        },
        {
            "name": "time_series_slot_id",
            "xml_name": "timeSeriesSlotId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "duration",
            "xml_name": "duration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "recurrence_information",
            "xml_name": "recurrenceInformation",
            "type": "ns_p:AbsoluteOrRecurringTimeElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeElementsType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "min_value",
            "xml_name": "minValue",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_value",
            "xml_name": "maxValue",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

