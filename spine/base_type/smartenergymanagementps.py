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
    from spine.base_type.operatingconstraints import OperatingConstraintsDurationDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsDurationDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsInterruptDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsInterruptDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationDataType
    from spine.base_type.powersequences import PowerSequenceAlternativesRelationDataElementsType
    from spine.base_type.powersequences import PowerSequenceAlternativesRelationDataType
    from spine.base_type.powersequences import PowerSequenceDescriptionDataElementsType
    from spine.base_type.powersequences import PowerSequenceDescriptionDataType
    from spine.base_type.powersequences import PowerSequenceScheduleConstraintsDataElementsType
    from spine.base_type.powersequences import PowerSequenceScheduleConstraintsDataType
    from spine.base_type.powersequences import PowerSequenceScheduleDataElementsType
    from spine.base_type.powersequences import PowerSequenceScheduleDataType
    from spine.base_type.powersequences import PowerSequenceSchedulePreferenceDataElementsType
    from spine.base_type.powersequences import PowerSequenceSchedulePreferenceDataType
    from spine.base_type.powersequences import PowerSequenceStateDataElementsType
    from spine.base_type.powersequences import PowerSequenceStateDataType
    from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsDataElementsType
    from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsDataType
    from spine.base_type.powersequences import PowerTimeSlotScheduleDataElementsType
    from spine.base_type.powersequences import PowerTimeSlotScheduleDataType
    from spine.base_type.powersequences import PowerTimeSlotValueDataElementsType
    from spine.base_type.powersequences import PowerTimeSlotValueDataType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.powersequences import AlternativesIdType
    from spine.simple_type.powersequences import PowerSequenceIdType
    from spine.simple_type.powersequences import PowerTimeSlotNumberType
    from spine.simple_type.smartenergymanagementps import Anonymous_4504021920
    from spine.simple_type.smartenergymanagementps import Anonymous_4504071968
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.measurement import MeasurementValueSourceType
    from spine.union_type.powersequences import PowerSequenceScopeType
    from spine.union_type.powersequences import PowerSequenceStateType
    from spine.union_type.powersequences import PowerTimeSlotValueTypeType



@spine_type('ns_p:Anonymous_4504178352', is_value_type=False, no_attrib_name=False)
class Anonymous_4504178352(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504178352 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
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


@spine_type('ns_p:SmartEnergyManagementPsPowerTimeSlotValueListElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPowerTimeSlotValueListElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPowerTimeSlotValueListElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_type",
            "xml_name": "valueType",
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
    ]


@spine_type('ns_p:Anonymous_4504175536', is_value_type=False, no_attrib_name=False)
class Anonymous_4504175536(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504175536 -> ComplexType
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


@spine_type('ns_p:Anonymous_4504085776', is_value_type=False, no_attrib_name=False)
class Anonymous_4504085776(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504085776 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:PowerTimeSlotValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotValueTypeType"
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


@spine_type('ns_p:SmartEnergyManagementPsPowerTimeSlotValueListType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPowerTimeSlotValueListType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPowerTimeSlotValueListType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:PowerTimeSlotValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotValueTypeType"
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


@spine_type('ns_p:Anonymous_4504076352', is_value_type=False, no_attrib_name=False)
class Anonymous_4504076352(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504076352 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4504162144', is_value_type=False, no_attrib_name=False)
class Anonymous_4504162144(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504162144 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "min_duration",
            "xml_name": "minDuration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_duration",
            "xml_name": "maxDuration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "optional_slot",
            "xml_name": "optionalSlot",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504161088', is_value_type=False, no_attrib_name=False)
class Anonymous_4504161088(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504161088 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
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
            "name": "default_duration",
            "xml_name": "defaultDuration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "duration_uncertainty",
            "xml_name": "durationUncertainty",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_activated",
            "xml_name": "slotActivated",
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


@spine_type('ns_p:SmartEnergyManagementPsPowerTimeSlotElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPowerTimeSlotElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPowerTimeSlotElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:Anonymous_4504175536",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504175536"
        },
        {
            "name": "default_duration",
            "xml_name": "defaultDuration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "duration_uncertainty",
            "xml_name": "durationUncertainty",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "slot_activated",
            "xml_name": "slotActivated",
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
            "name": "value_list",
            "xml_name": "valueList",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotValueListElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerTimeSlotValueListElementsType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:Anonymous_4504178352",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504178352"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "min_duration",
            "xml_name": "minDuration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_duration",
            "xml_name": "maxDuration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "optional_slot",
            "xml_name": "optionalSlot",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504062784', is_value_type=False, no_attrib_name=False)
class Anonymous_4504062784(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504062784 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "min_duration",
            "xml_name": "minDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "max_duration",
            "xml_name": "maxDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "optional_slot",
            "xml_name": "optionalSlot",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:Anonymous_4504061728', is_value_type=False, no_attrib_name=False)
class Anonymous_4504061728(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504061728 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
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
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "default_duration",
            "xml_name": "defaultDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "duration_uncertainty",
            "xml_name": "durationUncertainty",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "slot_activated",
            "xml_name": "slotActivated",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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


@spine_type('ns_p:SmartEnergyManagementPsPowerTimeSlotType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPowerTimeSlotType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPowerTimeSlotType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:Anonymous_4504076352",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504076352"
        },
        {
            "name": "default_duration",
            "xml_name": "defaultDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "duration_uncertainty",
            "xml_name": "durationUncertainty",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "slot_activated",
            "xml_name": "slotActivated",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:Anonymous_4504071968",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504071968"
        },
        {
            "name": "value_list",
            "xml_name": "valueList",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotValueListType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerTimeSlotValueListType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:Anonymous_4504085776",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "min_duration",
            "xml_name": "minDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "max_duration",
            "xml_name": "maxDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "optional_slot",
            "xml_name": "optionalSlot",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:Anonymous_4504133872', is_value_type=False, no_attrib_name=False)
class Anonymous_4504133872(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504133872 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "resume_energy_estimated",
            "xml_name": "resumeEnergyEstimated",
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
            "name": "energy_unit",
            "xml_name": "energyUnit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "resume_cost_estimated",
            "xml_name": "resumeCostEstimated",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504120656', is_value_type=False, no_attrib_name=False)
class Anonymous_4504120656(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504120656 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_min",
            "xml_name": "activeDurationMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_max",
            "xml_name": "activeDurationMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "pause_duration_min",
            "xml_name": "pauseDurationMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "pause_duration_max",
            "xml_name": "pauseDurationMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_sum_min",
            "xml_name": "activeDurationSumMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_sum_max",
            "xml_name": "activeDurationSumMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504119776', is_value_type=False, no_attrib_name=False)
class Anonymous_4504119776(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504119776 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_pausable",
            "xml_name": "isPausable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_stoppable",
            "xml_name": "isStoppable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "not_interruptible_at_high_power",
            "xml_name": "notInterruptibleAtHighPower",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_cycles_per_day",
            "xml_name": "maxCyclesPerDay",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504118896', is_value_type=False, no_attrib_name=False)
class Anonymous_4504118896(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504118896 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "greenest",
            "xml_name": "greenest",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cheapest",
            "xml_name": "cheapest",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504118016', is_value_type=False, no_attrib_name=False)
class Anonymous_4504118016(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504118016 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "latest_start_time",
            "xml_name": "latestStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "earliest_end_time",
            "xml_name": "earliestEndTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "optional_sequence",
            "xml_name": "optionalSequence",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504100704', is_value_type=False, no_attrib_name=False)
class Anonymous_4504100704(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504100704 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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


@spine_type('ns_p:Anonymous_4504099824', is_value_type=False, no_attrib_name=False)
class Anonymous_4504099824(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504099824 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_slot_number",
            "xml_name": "activeSlotNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "elapsed_slot_time",
            "xml_name": "elapsedSlotTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "remaining_slot_time",
            "xml_name": "remainingSlotTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "sequence_remote_controllable",
            "xml_name": "sequenceRemoteControllable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_repetition_number",
            "xml_name": "activeRepetitionNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "remaining_pause_time",
            "xml_name": "remainingPauseTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504098768', is_value_type=False, no_attrib_name=False)
class Anonymous_4504098768(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504098768 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
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
            "name": "positive_energy_direction",
            "xml_name": "positiveEnergyDirection",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "power_unit",
            "xml_name": "powerUnit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "energy_unit",
            "xml_name": "energyUnit",
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
            "name": "scope",
            "xml_name": "scope",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "task_identifier",
            "xml_name": "taskIdentifier",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "repetitions_total",
            "xml_name": "repetitionsTotal",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPowerSequenceElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPowerSequenceElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPowerSequenceElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
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
            "name": "power_unit",
            "xml_name": "powerUnit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "energy_unit",
            "xml_name": "energyUnit",
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
            "name": "task_identifier",
            "xml_name": "taskIdentifier",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "repetitions_total",
            "xml_name": "repetitionsTotal",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_slot_number",
            "xml_name": "activeSlotNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "elapsed_slot_time",
            "xml_name": "elapsedSlotTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "remaining_slot_time",
            "xml_name": "remainingSlotTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "sequence_remote_controllable",
            "xml_name": "sequenceRemoteControllable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_repetition_number",
            "xml_name": "activeRepetitionNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "remaining_pause_time",
            "xml_name": "remainingPauseTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "greenest",
            "xml_name": "greenest",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cheapest",
            "xml_name": "cheapest",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_pausable",
            "xml_name": "isPausable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_stoppable",
            "xml_name": "isStoppable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "max_cycles_per_day",
            "xml_name": "maxCyclesPerDay",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_min",
            "xml_name": "activeDurationMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_max",
            "xml_name": "activeDurationMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "pause_duration_min",
            "xml_name": "pauseDurationMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "pause_duration_max",
            "xml_name": "pauseDurationMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_sum_min",
            "xml_name": "activeDurationSumMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "active_duration_sum_max",
            "xml_name": "activeDurationSumMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "resume_energy_estimated",
            "xml_name": "resumeEnergyEstimated",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "resume_cost_estimated",
            "xml_name": "resumeCostEstimated",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
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
            "name": "power_time_slot",
            "xml_name": "powerTimeSlot",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerTimeSlotElementsType"
        },
        {
            "name": "schedule",
            "xml_name": "schedule",
            "type": "ns_p:Anonymous_4504161088",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504161088"
        },
        {
            "name": "value_list",
            "xml_name": "valueList",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotValueListElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerTimeSlotValueListElementsType"
        },
        {
            "name": "schedule_constraints",
            "xml_name": "scheduleConstraints",
            "type": "ns_p:Anonymous_4504162144",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504162144"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsAlternativesRelationElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsAlternativesRelationElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsAlternativesRelationElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alternatives_id",
            "xml_name": "alternativesId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4504016144', is_value_type=False, no_attrib_name=False)
class Anonymous_4504016144(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504016144 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "resume_energy_estimated",
            "xml_name": "resumeEnergyEstimated",
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
            "name": "energy_unit",
            "xml_name": "energyUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
        {
            "name": "resume_cost_estimated",
            "xml_name": "resumeCostEstimated",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
    ]


@spine_type('ns_p:Anonymous_4504015264', is_value_type=False, no_attrib_name=False)
class Anonymous_4504015264(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504015264 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "active_duration_min",
            "xml_name": "activeDurationMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "active_duration_max",
            "xml_name": "activeDurationMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "pause_duration_min",
            "xml_name": "pauseDurationMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "pause_duration_max",
            "xml_name": "pauseDurationMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "active_duration_sum_min",
            "xml_name": "activeDurationSumMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "active_duration_sum_max",
            "xml_name": "activeDurationSumMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4504006144', is_value_type=False, no_attrib_name=False)
class Anonymous_4504006144(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504006144 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "is_pausable",
            "xml_name": "isPausable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_stoppable",
            "xml_name": "isStoppable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "not_interruptible_at_high_power",
            "xml_name": "notInterruptibleAtHighPower",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "max_cycles_per_day",
            "xml_name": "maxCyclesPerDay",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:Anonymous_4504005264', is_value_type=False, no_attrib_name=False)
class Anonymous_4504005264(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504005264 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "greenest",
            "xml_name": "greenest",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "cheapest",
            "xml_name": "cheapest",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:Anonymous_4504004384', is_value_type=False, no_attrib_name=False)
class Anonymous_4504004384(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504004384 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "latest_start_time",
            "xml_name": "latestStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "earliest_end_time",
            "xml_name": "earliestEndTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "optional_sequence",
            "xml_name": "optionalSequence",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:Anonymous_4504003504', is_value_type=False, no_attrib_name=False)
class Anonymous_4504003504(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504003504 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4504002624', is_value_type=False, no_attrib_name=False)
class Anonymous_4504002624(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4504002624 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:PowerSequenceStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceStateType"
        },
        {
            "name": "active_slot_number",
            "xml_name": "activeSlotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
        },
        {
            "name": "elapsed_slot_time",
            "xml_name": "elapsedSlotTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "remaining_slot_time",
            "xml_name": "remainingSlotTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "sequence_remote_controllable",
            "xml_name": "sequenceRemoteControllable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "active_repetition_number",
            "xml_name": "activeRepetitionNumber",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "remaining_pause_time",
            "xml_name": "remainingPauseTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4503985136', is_value_type=False, no_attrib_name=False)
class Anonymous_4503985136(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:Anonymous_4503985136 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
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
            "name": "positive_energy_direction",
            "xml_name": "positiveEnergyDirection",
            "type": "ns_p:EnergyDirectionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyDirectionType"
        },
        {
            "name": "power_unit",
            "xml_name": "powerUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
        {
            "name": "energy_unit",
            "xml_name": "energyUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
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
            "name": "scope",
            "xml_name": "scope",
            "type": "ns_p:PowerSequenceScopeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScopeType"
        },
        {
            "name": "task_identifier",
            "xml_name": "taskIdentifier",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "repetitions_total",
            "xml_name": "repetitionsTotal",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPowerSequenceType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPowerSequenceType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPowerSequenceType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:Anonymous_4504021920",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504021920"
        },
        {
            "name": "power_unit",
            "xml_name": "powerUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
        {
            "name": "energy_unit",
            "xml_name": "energyUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
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
            "name": "task_identifier",
            "xml_name": "taskIdentifier",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "repetitions_total",
            "xml_name": "repetitionsTotal",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:PowerSequenceStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceStateType"
        },
        {
            "name": "active_slot_number",
            "xml_name": "activeSlotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
        },
        {
            "name": "elapsed_slot_time",
            "xml_name": "elapsedSlotTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "remaining_slot_time",
            "xml_name": "remainingSlotTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "sequence_remote_controllable",
            "xml_name": "sequenceRemoteControllable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "active_repetition_number",
            "xml_name": "activeRepetitionNumber",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "remaining_pause_time",
            "xml_name": "remainingPauseTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "greenest",
            "xml_name": "greenest",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "cheapest",
            "xml_name": "cheapest",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_pausable",
            "xml_name": "isPausable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_stoppable",
            "xml_name": "isStoppable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "max_cycles_per_day",
            "xml_name": "maxCyclesPerDay",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "active_duration_min",
            "xml_name": "activeDurationMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "active_duration_max",
            "xml_name": "activeDurationMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "pause_duration_min",
            "xml_name": "pauseDurationMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "pause_duration_max",
            "xml_name": "pauseDurationMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "active_duration_sum_min",
            "xml_name": "activeDurationSumMin",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "active_duration_sum_max",
            "xml_name": "activeDurationSumMax",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "resume_energy_estimated",
            "xml_name": "resumeEnergyEstimated",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "resume_cost_estimated",
            "xml_name": "resumeCostEstimated",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
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
            "name": "power_time_slot",
            "xml_name": "powerTimeSlot",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "schedule",
            "xml_name": "schedule",
            "type": "ns_p:Anonymous_4504061728",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504061728"
        },
        {
            "name": "value_list",
            "xml_name": "valueList",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotValueListType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerTimeSlotValueListType"
        },
        {
            "name": "schedule_constraints",
            "xml_name": "scheduleConstraints",
            "type": "ns_p:Anonymous_4504062784",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504062784"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsAlternativesRelationType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsAlternativesRelationType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsAlternativesRelationType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alternatives_id",
            "xml_name": "alternativesId",
            "type": "ns_p:AlternativesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlternativesIdType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsAlternativesElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsAlternativesElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsAlternativesElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "relation",
            "xml_name": "relation",
            "type": "ns_p:SmartEnergyManagementPsAlternativesRelationElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsAlternativesRelationElementsType"
        },
        {
            "name": "alternatives_id",
            "xml_name": "alternativesId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "power_sequence",
            "xml_name": "powerSequence",
            "type": "ns_p:SmartEnergyManagementPsPowerSequenceElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerSequenceElementsType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:Anonymous_4504098768",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504098768"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:Anonymous_4504099824",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504099824"
        },
        {
            "name": "schedule",
            "xml_name": "schedule",
            "type": "ns_p:Anonymous_4504100704",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504100704"
        },
        {
            "name": "schedule_constraints",
            "xml_name": "scheduleConstraints",
            "type": "ns_p:Anonymous_4504118016",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504118016"
        },
        {
            "name": "schedule_preference",
            "xml_name": "schedulePreference",
            "type": "ns_p:Anonymous_4504118896",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504118896"
        },
        {
            "name": "operating_constraints_interrupt",
            "xml_name": "operatingConstraintsInterrupt",
            "type": "ns_p:Anonymous_4504119776",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504119776"
        },
        {
            "name": "operating_constraints_duration",
            "xml_name": "operatingConstraintsDuration",
            "type": "ns_p:Anonymous_4504120656",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504120656"
        },
        {
            "name": "operating_constraints_resume_implication",
            "xml_name": "operatingConstraintsResumeImplication",
            "type": "ns_p:Anonymous_4504133872",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504133872"
        },
        {
            "name": "power_time_slot",
            "xml_name": "powerTimeSlot",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerTimeSlotElementsType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsAlternativesType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsAlternativesType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsAlternativesType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "relation",
            "xml_name": "relation",
            "type": "ns_p:SmartEnergyManagementPsAlternativesRelationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsAlternativesRelationType"
        },
        {
            "name": "alternatives_id",
            "xml_name": "alternativesId",
            "type": "ns_p:AlternativesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlternativesIdType"
        },
        {
            "name": "power_sequence",
            "xml_name": "powerSequence",
            "type": "ns_p:SmartEnergyManagementPsPowerSequenceType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:Anonymous_4503985136",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503985136"
        },
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:Anonymous_4504002624",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504002624"
        },
        {
            "name": "schedule",
            "xml_name": "schedule",
            "type": "ns_p:Anonymous_4504003504",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504003504"
        },
        {
            "name": "schedule_constraints",
            "xml_name": "scheduleConstraints",
            "type": "ns_p:Anonymous_4504004384",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504004384"
        },
        {
            "name": "schedule_preference",
            "xml_name": "schedulePreference",
            "type": "ns_p:Anonymous_4504005264",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504005264"
        },
        {
            "name": "operating_constraints_interrupt",
            "xml_name": "operatingConstraintsInterrupt",
            "type": "ns_p:Anonymous_4504006144",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504006144"
        },
        {
            "name": "operating_constraints_duration",
            "xml_name": "operatingConstraintsDuration",
            "type": "ns_p:Anonymous_4504015264",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504015264"
        },
        {
            "name": "operating_constraints_resume_implication",
            "xml_name": "operatingConstraintsResumeImplication",
            "type": "ns_p:Anonymous_4504016144",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4504016144"
        },
        {
            "name": "power_time_slot",
            "xml_name": "powerTimeSlot",
            "type": "ns_p:SmartEnergyManagementPsPowerTimeSlotType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPriceCalculationRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPriceCalculationRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPriceCalculationRequestCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPriceCalculationRequestCallType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPriceCalculationRequestCallType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPriceCalculationRequestCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsConfigurationRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsConfigurationRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsConfigurationRequestCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsConfigurationRequestCallType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsConfigurationRequestCallType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsConfigurationRequestCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPriceDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPriceDataSelectorsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPriceDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPriceDataElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPriceDataElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPriceDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "price",
            "xml_name": "price",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsPriceDataType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsPriceDataType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsPriceDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "price",
            "xml_name": "price",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsDataSelectorsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "alternatives_id",
            "xml_name": "alternativesId",
            "type": "ns_p:AlternativesIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlternativesIdType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "slot_number",
            "xml_name": "slotNumber",
            "type": "ns_p:PowerTimeSlotNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotNumberType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:PowerTimeSlotValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotValueTypeType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsDataElementsType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsDataElementsType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_remote_controllable",
            "xml_name": "nodeRemoteControllable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "supports_single_slot_scheduling_only",
            "xml_name": "supportsSingleSlotSchedulingOnly",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "alternatives_count",
            "xml_name": "alternativesCount",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "total_sequences_count_max",
            "xml_name": "totalSequencesCountMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "supports_reselection",
            "xml_name": "supportsReselection",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "alternatives",
            "xml_name": "alternatives",
            "type": "ns_p:SmartEnergyManagementPsAlternativesElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsAlternativesElementsType"
        },
        {
            "name": "relation",
            "xml_name": "relation",
            "type": "ns_p:SmartEnergyManagementPsAlternativesRelationElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsAlternativesRelationElementsType"
        },
        {
            "name": "power_sequence",
            "xml_name": "powerSequence",
            "type": "ns_p:SmartEnergyManagementPsPowerSequenceElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPowerSequenceElementsType"
        },
    ]


@spine_type('ns_p:SmartEnergyManagementPsDataType', is_value_type=False, no_attrib_name=False)
class SmartEnergyManagementPsDataType(SpineBase): # EEBus_SPINE_TS_SmartEnergyManagementPs.xsd:ns_p:SmartEnergyManagementPsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_remote_controllable",
            "xml_name": "nodeRemoteControllable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "supports_single_slot_scheduling_only",
            "xml_name": "supportsSingleSlotSchedulingOnly",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "alternatives_count",
            "xml_name": "alternativesCount",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "total_sequences_count_max",
            "xml_name": "totalSequencesCountMax",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "supports_reselection",
            "xml_name": "supportsReselection",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "alternatives",
            "xml_name": "alternatives",
            "type": "ns_p:SmartEnergyManagementPsAlternativesType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "relation",
            "xml_name": "relation",
            "type": "ns_p:SmartEnergyManagementPsAlternativesRelationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsAlternativesRelationType"
        },
        {
            "name": "power_sequence",
            "xml_name": "powerSequence",
            "type": "ns_p:SmartEnergyManagementPsPowerSequenceType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]

