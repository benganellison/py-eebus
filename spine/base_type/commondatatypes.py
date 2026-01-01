# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.enums.commondatatypes import MonthType
    from spine.simple_type.commondatatypes import AddressDeviceType
    from spine.simple_type.commondatatypes import AddressEntityType
    from spine.simple_type.commondatatypes import AddressFeatureType
    from spine.simple_type.commondatatypes import CalendarWeekType
    from spine.simple_type.commondatatypes import DayOfMonthType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import FunctionType
    from spine.union_type.commondatatypes import OccurrenceType
    from spine.union_type.commondatatypes import RecurringIntervalType



@spine_type('ns_p:ElementTagType', is_value_type=False, no_attrib_name=False)
class ElementTagType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ElementTagType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:PossibleOperationsClassifierType', is_value_type=False, no_attrib_name=False)
class PossibleOperationsClassifierType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:PossibleOperationsClassifierType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "partial",
            "xml_name": "partial",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:PossibleOperationsWriteType', is_value_type=False, no_attrib_name=False)
class PossibleOperationsWriteType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:PossibleOperationsWriteType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "partial",
            "xml_name": "partial",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:PossibleOperationsReadType', is_value_type=False, no_attrib_name=False)
class PossibleOperationsReadType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:PossibleOperationsReadType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "partial",
            "xml_name": "partial",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceAddressElementsType', is_value_type=False, no_attrib_name=False)
class DeviceAddressElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:DeviceAddressElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceAddressType', is_value_type=False, no_attrib_name=False)
class DeviceAddressType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:DeviceAddressType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
    ]


@spine_type('ns_p:ScaledNumberElementsType', is_value_type=False, no_attrib_name=False)
class ScaledNumberElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaledNumberElementsType -> ComplexType
    _MEMBER_INFO = [
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


@spine_type('ns_p:ScaledNumberType', is_value_type=False, no_attrib_name=False)
class ScaledNumberType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaledNumberType -> ComplexType
    _MEMBER_INFO = [
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


@spine_type('ns_p:PossibleOperationsElementsType', is_value_type=False, no_attrib_name=False)
class PossibleOperationsElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:PossibleOperationsElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "read",
            "xml_name": "read",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "write",
            "xml_name": "write",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:PossibleOperationsType', is_value_type=False, no_attrib_name=False)
class PossibleOperationsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:PossibleOperationsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "read",
            "xml_name": "read",
            "type": "ns_p:PossibleOperationsReadType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsReadType"
        },
        {
            "name": "write",
            "xml_name": "write",
            "type": "ns_p:PossibleOperationsWriteType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsWriteType"
        },
    ]


@spine_type('ns_p:EntityAddressElementsType', is_value_type=False, no_attrib_name=False)
class EntityAddressElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:EntityAddressElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:EntityAddressType', is_value_type=False, no_attrib_name=False)
class EntityAddressType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:EntityAddressType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:AddressEntityType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:ScaledNumberRangeElementsType', is_value_type=False, no_attrib_name=False)
class ScaledNumberRangeElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaledNumberRangeElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "min",
            "xml_name": "min",
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
            "name": "max",
            "xml_name": "max",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:ScaledNumberRangeType', is_value_type=False, no_attrib_name=False)
class ScaledNumberRangeType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaledNumberRangeType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "min",
            "xml_name": "min",
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
            "name": "max",
            "xml_name": "max",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:DaysOfWeekType', is_value_type=False, no_attrib_name=False)
class DaysOfWeekType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:DaysOfWeekType -> ComplexType
    _MEMBER_INFO = [
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
    ]


@spine_type('ns_p:FunctionPropertyElementsType', is_value_type=False, no_attrib_name=False)
class FunctionPropertyElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:FunctionPropertyElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "possible_operations",
            "xml_name": "possibleOperations",
            "type": "ns_p:PossibleOperationsElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsElementsType"
        },
        {
            "name": "read",
            "xml_name": "read",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "write",
            "xml_name": "write",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:FunctionPropertyType', is_value_type=False, no_attrib_name=False)
class FunctionPropertyType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:FunctionPropertyType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:FunctionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FunctionType"
        },
        {
            "name": "possible_operations",
            "xml_name": "possibleOperations",
            "type": "ns_p:PossibleOperationsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsType"
        },
        {
            "name": "read",
            "xml_name": "read",
            "type": "ns_p:PossibleOperationsReadType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsReadType"
        },
        {
            "name": "write",
            "xml_name": "write",
            "type": "ns_p:PossibleOperationsWriteType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsWriteType"
        },
    ]


@spine_type('ns_p:FeatureAddressElementsType', is_value_type=False, no_attrib_name=False)
class FeatureAddressElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:FeatureAddressElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "feature",
            "xml_name": "feature",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:FeatureAddressType', is_value_type=False, no_attrib_name=False)
class FeatureAddressType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:FeatureAddressType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:AddressEntityType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "feature",
            "xml_name": "feature",
            "type": "ns_p:AddressFeatureType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressFeatureType"
        },
    ]


@spine_type('ns_p:ScaledNumberSetElementsType', is_value_type=False, no_attrib_name=False)
class ScaledNumberSetElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaledNumberSetElementsType -> ComplexType
    _MEMBER_INFO = [
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
            "name": "range",
            "xml_name": "range",
            "type": "ns_p:ScaledNumberRangeElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberRangeElementsType"
        },
        {
            "name": "min",
            "xml_name": "min",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "max",
            "xml_name": "max",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:ScaledNumberSetType', is_value_type=False, no_attrib_name=False)
class ScaledNumberSetType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:ScaledNumberSetType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "range",
            "xml_name": "range",
            "type": "ns_p:ScaledNumberRangeType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "min",
            "xml_name": "min",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "max",
            "xml_name": "max",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:RecurrenceInformationElementsType', is_value_type=False, no_attrib_name=False)
class RecurrenceInformationElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:RecurrenceInformationElementsType -> ComplexType
    _MEMBER_INFO = [
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
    ]


@spine_type('ns_p:RecurrenceInformationType', is_value_type=False, no_attrib_name=False)
class RecurrenceInformationType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:RecurrenceInformationType -> ComplexType
    _MEMBER_INFO = [
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
    ]


@spine_type('ns_p:AbsoluteOrRecurringTimeElementsType', is_value_type=False, no_attrib_name=False)
class AbsoluteOrRecurringTimeElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:AbsoluteOrRecurringTimeElementsType -> ComplexType
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


@spine_type('ns_p:AbsoluteOrRecurringTimeType', is_value_type=False, no_attrib_name=False)
class AbsoluteOrRecurringTimeType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:AbsoluteOrRecurringTimeType -> ComplexType
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


@spine_type('ns_p:TimestampIntervalType', is_value_type=False, no_attrib_name=False)
class TimestampIntervalType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:TimestampIntervalType -> ComplexType
    _MEMBER_INFO = [
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


@spine_type('ns_p:TimePeriodElementsType', is_value_type=False, no_attrib_name=False)
class TimePeriodElementsType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:TimePeriodElementsType -> ComplexType
    _MEMBER_INFO = [
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


@spine_type('ns_p:TimePeriodType', is_value_type=False, no_attrib_name=False)
class TimePeriodType(SpineBase): # EEBus_SPINE_TS_CommonDataTypes.xsd:ns_p:TimePeriodType -> ComplexType
    _MEMBER_INFO = [
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

