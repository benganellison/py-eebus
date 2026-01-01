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
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.powersequences import AlternativesIdType
    from spine.simple_type.powersequences import PowerSequenceIdType
    from spine.simple_type.powersequences import PowerTimeSlotNumberType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.measurement import MeasurementValueSourceType
    from spine.union_type.powersequences import PowerSequenceScopeType
    from spine.union_type.powersequences import PowerSequenceStateType
    from spine.union_type.powersequences import PowerTimeSlotValueTypeType



@spine_type('ns_p:PowerSequenceSchedulePreferenceDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceSchedulePreferenceDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceDataType -> ComplexType
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


@spine_type('ns_p:PowerSequencePriceDataType', is_value_type=False, no_attrib_name=False)
class PowerSequencePriceDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceDataType -> ComplexType
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
            "name": "potential_start_time",
            "xml_name": "potentialStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
    ]


@spine_type('ns_p:PowerSequenceScheduleConstraintsDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleConstraintsDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsDataType -> ComplexType
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
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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


@spine_type('ns_p:PowerSequenceScheduleDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleDataType -> ComplexType
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


@spine_type('ns_p:PowerSequenceStateDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceStateDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateDataType -> ComplexType
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


@spine_type('ns_p:PowerSequenceDescriptionDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceDescriptionDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionDataType -> ComplexType
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


@spine_type('ns_p:PowerSequenceAlternativesRelationDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceAlternativesRelationDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationDataType -> ComplexType
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


@spine_type('ns_p:PowerTimeSlotScheduleConstraintsDataType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleConstraintsDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsDataType -> ComplexType
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
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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


@spine_type('ns_p:PowerTimeSlotValueDataType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotValueDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueDataType -> ComplexType
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


@spine_type('ns_p:PowerTimeSlotScheduleDataType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleDataType -> ComplexType
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


@spine_type('ns_p:PowerSequencePriceCalculationRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequencePriceCalculationRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceCalculationRequestCallElementsType -> ComplexType
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
            "name": "potential_start_time",
            "xml_name": "potentialStartTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:PowerSequencePriceCalculationRequestCallType', is_value_type=False, no_attrib_name=False)
class PowerSequencePriceCalculationRequestCallType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceCalculationRequestCallType -> ComplexType
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
            "name": "potential_start_time",
            "xml_name": "potentialStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:PowerSequenceScheduleConfigurationRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleConfigurationRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConfigurationRequestCallElementsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceScheduleConfigurationRequestCallType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleConfigurationRequestCallType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConfigurationRequestCallType -> ComplexType
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


@spine_type('ns_p:PowerSequenceNodeScheduleInformationDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceNodeScheduleInformationDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceNodeScheduleInformationDataElementsType -> ComplexType
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
    ]


@spine_type('ns_p:PowerSequenceNodeScheduleInformationDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceNodeScheduleInformationDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceNodeScheduleInformationDataType -> ComplexType
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
    ]


@spine_type('ns_p:PowerSequenceSchedulePreferenceListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceSchedulePreferenceListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceSchedulePreferenceListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceSchedulePreferenceListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_schedule_preference_data",
            "xml_name": "powerSequenceSchedulePreferenceData",
            "type": "ns_p:PowerSequenceSchedulePreferenceDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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


@spine_type('ns_p:PowerSequenceSchedulePreferenceDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceSchedulePreferenceDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerSequencePriceListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequencePriceListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceListDataSelectorsType -> ComplexType
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
            "name": "potential_start_time_interval",
            "xml_name": "potentialStartTimeInterval",
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


@spine_type('ns_p:PowerSequencePriceListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequencePriceListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_price_data",
            "xml_name": "powerSequencePriceData",
            "type": "ns_p:PowerSequencePriceDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "potential_start_time",
            "xml_name": "potentialStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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


@spine_type('ns_p:PowerSequencePriceDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequencePriceDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceDataElementsType -> ComplexType
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
            "name": "potential_start_time",
            "xml_name": "potentialStartTime",
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:PowerSequenceScheduleConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceScheduleConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_schedule_constraints_data",
            "xml_name": "powerSequenceScheduleConstraintsData",
            "type": "ns_p:PowerSequenceScheduleConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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


@spine_type('ns_p:PowerSequenceScheduleConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceScheduleListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceScheduleListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_schedule_data",
            "xml_name": "powerSequenceScheduleData",
            "type": "ns_p:PowerSequenceScheduleDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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


@spine_type('ns_p:PowerSequenceScheduleDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceScheduleDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceStateListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceStateListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceStateListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceStateListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_state_data",
            "xml_name": "powerSequenceStateData",
            "type": "ns_p:PowerSequenceStateDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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


@spine_type('ns_p:PowerSequenceStateDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceStateDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_description_data",
            "xml_name": "powerSequenceDescriptionData",
            "type": "ns_p:PowerSequenceDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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


@spine_type('ns_p:PowerSequenceDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerSequenceAlternativesRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceAlternativesRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationListDataSelectorsType -> ComplexType
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
    ]


@spine_type('ns_p:PowerSequenceAlternativesRelationListDataType', is_value_type=False, no_attrib_name=False)
class PowerSequenceAlternativesRelationListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_sequence_alternatives_relation_data",
            "xml_name": "powerSequenceAlternativesRelationData",
            "type": "ns_p:PowerSequenceAlternativesRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:PowerSequenceAlternativesRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerSequenceAlternativesRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerTimeSlotScheduleConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsListDataSelectorsType -> ComplexType
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
    ]


@spine_type('ns_p:PowerTimeSlotScheduleConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_time_slot_schedule_constraints_data",
            "xml_name": "powerTimeSlotScheduleConstraintsData",
            "type": "ns_p:PowerTimeSlotScheduleConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "earliest_start_time",
            "xml_name": "earliestStartTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "latest_end_time",
            "xml_name": "latestEndTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
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


@spine_type('ns_p:PowerTimeSlotScheduleConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerTimeSlotValueListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotValueListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueListDataSelectorsType -> ComplexType
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
    ]


@spine_type('ns_p:PowerTimeSlotValueListDataType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotValueListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_time_slot_value_data",
            "xml_name": "powerTimeSlotValueData",
            "type": "ns_p:PowerTimeSlotValueDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:PowerTimeSlotValueDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotValueDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueDataElementsType -> ComplexType
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


@spine_type('ns_p:PowerTimeSlotScheduleListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleListDataSelectorsType -> ComplexType
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
    ]


@spine_type('ns_p:PowerTimeSlotScheduleListDataType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleListDataType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "power_time_slot_schedule_data",
            "xml_name": "powerTimeSlotScheduleData",
            "type": "ns_p:PowerTimeSlotScheduleDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
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


@spine_type('ns_p:PowerTimeSlotScheduleDataElementsType', is_value_type=False, no_attrib_name=False)
class PowerTimeSlotScheduleDataElementsType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleDataElementsType -> ComplexType
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

