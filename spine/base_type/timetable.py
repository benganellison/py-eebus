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
    from spine.enums.commondatatypes import MonthType
    from spine.simple_type.commondatatypes import CalendarWeekType
    from spine.simple_type.commondatatypes import DayOfMonthType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.timetable import TimeSlotCountType
    from spine.simple_type.timetable import TimeSlotIdType
    from spine.simple_type.timetable import TimeTableIdType
    from spine.union_type.commondatatypes import OccurrenceType
    from spine.union_type.commondatatypes import RecurringIntervalType
    from spine.union_type.timetable import TimeSlotTimeModeType



@spine_type('ns_p:TimeTableDescriptionDataType', is_value_type=False, no_attrib_name=False)
class TimeTableDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionDataType -> ComplexType
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
            "name": "time_slot_count_changeable",
            "xml_name": "timeSlotCountChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_slot_times_changeable",
            "xml_name": "timeSlotTimesChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_slot_time_mode",
            "xml_name": "timeSlotTimeMode",
            "type": "ns_p:TimeSlotTimeModeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotTimeModeType"
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


@spine_type('ns_p:TimeTableConstraintsDataType', is_value_type=False, no_attrib_name=False)
class TimeTableConstraintsDataType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsDataType -> ComplexType
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


@spine_type('ns_p:TimeTableDataType', is_value_type=False, no_attrib_name=False)
class TimeTableDataType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDataType -> ComplexType
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


@spine_type('ns_p:TimeTableDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TimeTableDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
    ]


@spine_type('ns_p:TimeTableDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class TimeTableDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_description_data",
            "xml_name": "timeTableDescriptionData",
            "type": "ns_p:TimeTableDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "time_slot_count_changeable",
            "xml_name": "timeSlotCountChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_slot_times_changeable",
            "xml_name": "timeSlotTimesChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_slot_time_mode",
            "xml_name": "timeSlotTimeMode",
            "type": "ns_p:TimeSlotTimeModeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotTimeModeType"
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


@spine_type('ns_p:TimeTableDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeTableDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionDataElementsType -> ComplexType
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
            "name": "time_slot_count_changeable",
            "xml_name": "timeSlotCountChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_slot_times_changeable",
            "xml_name": "timeSlotTimesChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_slot_time_mode",
            "xml_name": "timeSlotTimeMode",
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


@spine_type('ns_p:TimeTableConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TimeTableConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
    ]


@spine_type('ns_p:TimeTableConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class TimeTableConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_constraints_data",
            "xml_name": "timeTableConstraintsData",
            "type": "ns_p:TimeTableConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
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


@spine_type('ns_p:TimeTableConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeTableConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsDataElementsType -> ComplexType
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


@spine_type('ns_p:TimeTableListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TimeTableListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableListDataSelectorsType -> ComplexType
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
    ]


@spine_type('ns_p:TimeTableListDataType', is_value_type=False, no_attrib_name=False)
class TimeTableListDataType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "time_table_data",
            "xml_name": "timeTableData",
            "type": "ns_p:TimeTableDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:AbsoluteOrRecurringTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRecurringTimeType"
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


@spine_type('ns_p:TimeTableDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeTableDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDataElementsType -> ComplexType
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

