# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberRangeElementsType
    from spine.base_type.commondatatypes import ScaledNumberRangeType
    from spine.base_type.commondatatypes import ScaledNumberSetElementsType
    from spine.base_type.commondatatypes import ScaledNumberSetType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.electricalconnection import ElectricalConnectionCharacteristicIdType
    from spine.simple_type.electricalconnection import ElectricalConnectionIdType
    from spine.simple_type.electricalconnection import ElectricalConnectionParameterIdType
    from spine.simple_type.measurement import MeasurementIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import EnergyModeType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.electricalconnection import ElectricalConnectionAcMeasurementTypeType
    from spine.union_type.electricalconnection import ElectricalConnectionCharacteristicContextType
    from spine.union_type.electricalconnection import ElectricalConnectionCharacteristicTypeType
    from spine.union_type.electricalconnection import ElectricalConnectionMeasurandVariantType
    from spine.union_type.electricalconnection import ElectricalConnectionPhaseNameType
    from spine.union_type.electricalconnection import ElectricalConnectionVoltageTypeType



@spine_type('ns_p:ElectricalConnectionDescriptionDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionDescriptionDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "power_supply_type",
            "xml_name": "powerSupplyType",
            "type": "ns_p:ElectricalConnectionVoltageTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionVoltageTypeType"
        },
        {
            "name": "ac_connected_phases",
            "xml_name": "acConnectedPhases",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "ac_rms_period_duration",
            "xml_name": "acRmsPeriodDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
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


@spine_type('ns_p:ElectricalConnectionStateDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionStateDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
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
            "name": "current_energy_mode",
            "xml_name": "currentEnergyMode",
            "type": "ns_p:EnergyModeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyModeType"
        },
        {
            "name": "consumption_time",
            "xml_name": "consumptionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "production_time",
            "xml_name": "productionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "total_consumption_time",
            "xml_name": "totalConsumptionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "total_production_time",
            "xml_name": "totalProductionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:ElectricalConnectionCharacteristicDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionCharacteristicDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
        },
        {
            "name": "characteristic_id",
            "xml_name": "characteristicId",
            "type": "ns_p:ElectricalConnectionCharacteristicIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicIdType"
        },
        {
            "name": "characteristic_context",
            "xml_name": "characteristicContext",
            "type": "ns_p:ElectricalConnectionCharacteristicContextType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicContextType"
        },
        {
            "name": "characteristic_type",
            "xml_name": "characteristicType",
            "type": "ns_p:ElectricalConnectionCharacteristicTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicTypeType"
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
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionPermittedValueSetDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionPermittedValueSetDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
        },
        {
            "name": "permitted_value_set",
            "xml_name": "permittedValueSet",
            "type": "ns_p:ScaledNumberSetType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "range",
            "xml_name": "range",
            "type": "ns_p:ScaledNumberRangeType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:ElectricalConnectionParameterDescriptionDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionParameterDescriptionDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
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
            "name": "voltage_type",
            "xml_name": "voltageType",
            "type": "ns_p:ElectricalConnectionVoltageTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionVoltageTypeType"
        },
        {
            "name": "ac_measured_phases",
            "xml_name": "acMeasuredPhases",
            "type": "ns_p:ElectricalConnectionPhaseNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPhaseNameType"
        },
        {
            "name": "ac_measured_in_reference_to",
            "xml_name": "acMeasuredInReferenceTo",
            "type": "ns_p:ElectricalConnectionPhaseNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPhaseNameType"
        },
        {
            "name": "ac_measurement_type",
            "xml_name": "acMeasurementType",
            "type": "ns_p:ElectricalConnectionAcMeasurementTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionAcMeasurementTypeType"
        },
        {
            "name": "ac_measurement_variant",
            "xml_name": "acMeasurementVariant",
            "type": "ns_p:ElectricalConnectionMeasurandVariantType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionMeasurandVariantType"
        },
        {
            "name": "ac_measured_harmonic",
            "xml_name": "acMeasuredHarmonic",
            "type": "xs:unsignedByte",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
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


@spine_type('ns_p:ElectricalConnectionDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
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


@spine_type('ns_p:ElectricalConnectionDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_description_data",
            "xml_name": "electricalConnectionDescriptionData",
            "type": "ns_p:ElectricalConnectionDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "power_supply_type",
            "xml_name": "powerSupplyType",
            "type": "ns_p:ElectricalConnectionVoltageTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionVoltageTypeType"
        },
        {
            "name": "ac_connected_phases",
            "xml_name": "acConnectedPhases",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "ac_rms_period_duration",
            "xml_name": "acRmsPeriodDuration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
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


@spine_type('ns_p:ElectricalConnectionDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "power_supply_type",
            "xml_name": "powerSupplyType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_connected_phases",
            "xml_name": "acConnectedPhases",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_rms_period_duration",
            "xml_name": "acRmsPeriodDuration",
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


@spine_type('ns_p:ElectricalConnectionStateListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionStateListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionStateListDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionStateListDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_state_data",
            "xml_name": "electricalConnectionStateData",
            "type": "ns_p:ElectricalConnectionStateDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
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
            "name": "current_energy_mode",
            "xml_name": "currentEnergyMode",
            "type": "ns_p:EnergyModeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyModeType"
        },
        {
            "name": "consumption_time",
            "xml_name": "consumptionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "production_time",
            "xml_name": "productionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "total_consumption_time",
            "xml_name": "totalConsumptionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "total_production_time",
            "xml_name": "totalProductionTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:ElectricalConnectionStateDataElementsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionStateDataElementsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
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
            "name": "current_energy_mode",
            "xml_name": "currentEnergyMode",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "consumption_time",
            "xml_name": "consumptionTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "production_time",
            "xml_name": "productionTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "total_consumption_time",
            "xml_name": "totalConsumptionTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "total_production_time",
            "xml_name": "totalProductionTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionCharacteristicListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionCharacteristicListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
        },
        {
            "name": "characteristic_id",
            "xml_name": "characteristicId",
            "type": "ns_p:ElectricalConnectionCharacteristicIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicIdType"
        },
        {
            "name": "characteristic_context",
            "xml_name": "characteristicContext",
            "type": "ns_p:ElectricalConnectionCharacteristicContextType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicContextType"
        },
        {
            "name": "characteristic_type",
            "xml_name": "characteristicType",
            "type": "ns_p:ElectricalConnectionCharacteristicTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicTypeType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionCharacteristicListDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionCharacteristicListDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_characteristic_data",
            "xml_name": "electricalConnectionCharacteristicData",
            "type": "ns_p:ElectricalConnectionCharacteristicDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
        },
        {
            "name": "characteristic_id",
            "xml_name": "characteristicId",
            "type": "ns_p:ElectricalConnectionCharacteristicIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicIdType"
        },
        {
            "name": "characteristic_context",
            "xml_name": "characteristicContext",
            "type": "ns_p:ElectricalConnectionCharacteristicContextType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicContextType"
        },
        {
            "name": "characteristic_type",
            "xml_name": "characteristicType",
            "type": "ns_p:ElectricalConnectionCharacteristicTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicTypeType"
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
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionCharacteristicDataElementsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionCharacteristicDataElementsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "characteristic_id",
            "xml_name": "characteristicId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "characteristic_context",
            "xml_name": "characteristicContext",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "characteristic_type",
            "xml_name": "characteristicType",
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
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionPermittedValueSetListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionPermittedValueSetListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionPermittedValueSetListDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionPermittedValueSetListDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_permitted_value_set_data",
            "xml_name": "electricalConnectionPermittedValueSetData",
            "type": "ns_p:ElectricalConnectionPermittedValueSetDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
        },
        {
            "name": "permitted_value_set",
            "xml_name": "permittedValueSet",
            "type": "ns_p:ScaledNumberSetType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:ElectricalConnectionPermittedValueSetDataElementsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionPermittedValueSetDataElementsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "permitted_value_set",
            "xml_name": "permittedValueSet",
            "type": "ns_p:ScaledNumberSetElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberSetElementsType"
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
            "name": "range",
            "xml_name": "range",
            "type": "ns_p:ScaledNumberRangeElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberRangeElementsType"
        },
    ]


@spine_type('ns_p:ElectricalConnectionParameterDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionParameterDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
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


@spine_type('ns_p:ElectricalConnectionParameterDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionParameterDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_parameter_description_data",
            "xml_name": "electricalConnectionParameterDescriptionData",
            "type": "ns_p:ElectricalConnectionParameterDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElectricalConnectionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionIdType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
            "type": "ns_p:ElectricalConnectionParameterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterIdType"
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
            "name": "voltage_type",
            "xml_name": "voltageType",
            "type": "ns_p:ElectricalConnectionVoltageTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionVoltageTypeType"
        },
        {
            "name": "ac_measured_phases",
            "xml_name": "acMeasuredPhases",
            "type": "ns_p:ElectricalConnectionPhaseNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPhaseNameType"
        },
        {
            "name": "ac_measured_in_reference_to",
            "xml_name": "acMeasuredInReferenceTo",
            "type": "ns_p:ElectricalConnectionPhaseNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPhaseNameType"
        },
        {
            "name": "ac_measurement_type",
            "xml_name": "acMeasurementType",
            "type": "ns_p:ElectricalConnectionAcMeasurementTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionAcMeasurementTypeType"
        },
        {
            "name": "ac_measurement_variant",
            "xml_name": "acMeasurementVariant",
            "type": "ns_p:ElectricalConnectionMeasurandVariantType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionMeasurandVariantType"
        },
        {
            "name": "ac_measured_harmonic",
            "xml_name": "acMeasuredHarmonic",
            "type": "xs:unsignedByte",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
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


@spine_type('ns_p:ElectricalConnectionParameterDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class ElectricalConnectionParameterDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "electrical_connection_id",
            "xml_name": "electricalConnectionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "parameter_id",
            "xml_name": "parameterId",
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
            "name": "voltage_type",
            "xml_name": "voltageType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_measured_phases",
            "xml_name": "acMeasuredPhases",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_measured_in_reference_to",
            "xml_name": "acMeasuredInReferenceTo",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_measurement_type",
            "xml_name": "acMeasurementType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_measurement_variant",
            "xml_name": "acMeasurementVariant",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "ac_measured_harmonic",
            "xml_name": "acMeasuredHarmonic",
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

