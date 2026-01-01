# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.powersequences import PowerSequenceIdType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import UnitOfMeasurementType



@spine_type('ns_p:OperatingConstraintsResumeImplicationDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsResumeImplicationDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsResumeImplicationDataType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsPowerLevelDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerLevelDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerLevelDataType -> ComplexType
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
            "name": "power",
            "xml_name": "power",
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
    ]


@spine_type('ns_p:OperatingConstraintsPowerRangeDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerRangeDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerRangeDataType -> ComplexType
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
            "name": "power_min",
            "xml_name": "powerMin",
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
            "name": "power_max",
            "xml_name": "powerMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "energy_min",
            "xml_name": "energyMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "energy_max",
            "xml_name": "energyMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:OperatingConstraintsPowerDescriptionDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerDescriptionDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerDescriptionDataType -> ComplexType
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
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]


@spine_type('ns_p:OperatingConstraintsDurationDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsDurationDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsDurationDataType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsInterruptDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsInterruptDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsInterruptDataType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsResumeImplicationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsResumeImplicationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsResumeImplicationListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsResumeImplicationListDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsResumeImplicationListDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsResumeImplicationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operating_constraints_resume_implication_data",
            "xml_name": "operatingConstraintsResumeImplicationData",
            "type": "ns_p:OperatingConstraintsResumeImplicationDataType",
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
            "name": "resume_energy_estimated",
            "xml_name": "resumeEnergyEstimated",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
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


@spine_type('ns_p:OperatingConstraintsResumeImplicationDataElementsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsResumeImplicationDataElementsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsResumeImplicationDataElementsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsPowerLevelListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerLevelListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerLevelListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsPowerLevelListDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerLevelListDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerLevelListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operating_constraints_power_level_data",
            "xml_name": "operatingConstraintsPowerLevelData",
            "type": "ns_p:OperatingConstraintsPowerLevelDataType",
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
            "name": "power",
            "xml_name": "power",
            "type": "ns_p:ScaledNumberType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:OperatingConstraintsPowerLevelDataElementsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerLevelDataElementsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerLevelDataElementsType -> ComplexType
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
            "name": "power",
            "xml_name": "power",
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


@spine_type('ns_p:OperatingConstraintsPowerRangeListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerRangeListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerRangeListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsPowerRangeListDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerRangeListDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerRangeListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operating_constraints_power_range_data",
            "xml_name": "operatingConstraintsPowerRangeData",
            "type": "ns_p:OperatingConstraintsPowerRangeDataType",
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
            "name": "power_min",
            "xml_name": "powerMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "power_max",
            "xml_name": "powerMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "energy_min",
            "xml_name": "energyMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "energy_max",
            "xml_name": "energyMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:OperatingConstraintsPowerRangeDataElementsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerRangeDataElementsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerRangeDataElementsType -> ComplexType
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
            "name": "power_min",
            "xml_name": "powerMin",
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
            "name": "power_max",
            "xml_name": "powerMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "energy_min",
            "xml_name": "energyMin",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "energy_max",
            "xml_name": "energyMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:OperatingConstraintsPowerDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerDescriptionListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsPowerDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operating_constraints_power_description_data",
            "xml_name": "operatingConstraintsPowerDescriptionData",
            "type": "ns_p:OperatingConstraintsPowerDescriptionDataType",
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
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]


@spine_type('ns_p:OperatingConstraintsPowerDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsPowerDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsPowerDescriptionDataElementsType -> ComplexType
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
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:OperatingConstraintsDurationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsDurationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsDurationListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsDurationListDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsDurationListDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsDurationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operating_constraints_duration_data",
            "xml_name": "operatingConstraintsDurationData",
            "type": "ns_p:OperatingConstraintsDurationDataType",
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


@spine_type('ns_p:OperatingConstraintsDurationDataElementsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsDurationDataElementsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsDurationDataElementsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsInterruptListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsInterruptListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsInterruptListDataSelectorsType -> ComplexType
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


@spine_type('ns_p:OperatingConstraintsInterruptListDataType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsInterruptListDataType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsInterruptListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operating_constraints_interrupt_data",
            "xml_name": "operatingConstraintsInterruptData",
            "type": "ns_p:OperatingConstraintsInterruptDataType",
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


@spine_type('ns_p:OperatingConstraintsInterruptDataElementsType', is_value_type=False, no_attrib_name=False)
class OperatingConstraintsInterruptDataElementsType(SpineBase): # EEBus_SPINE_TS_OperatingConstraints.xsd:ns_p:OperatingConstraintsInterruptDataElementsType -> ComplexType
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

