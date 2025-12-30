# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.base_type.commondatatypes import TimestampIntervalType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.powersequences import PowerSequenceIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import EnergyDirectionType
    from spine.union_type.commondatatypes import EnergyModeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.directcontrol import DirectControlActivityStateType



@spine_type('ns_p:DirectControlActivityDataType', is_value_type=False, no_attrib_name=False)
class DirectControlActivityDataType(SpineBase): # EEBus_SPINE_TS_DirectControl.xsd:ns_p:DirectControlActivityDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "activity_state",
            "xml_name": "activityState",
            "type": "ns_p:DirectControlActivityStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlActivityStateType"
        },
        {
            "name": "is_activity_state_changeable",
            "xml_name": "isActivityStateChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "energy_mode",
            "xml_name": "energyMode",
            "type": "ns_p:EnergyModeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyModeType"
        },
        {
            "name": "is_energy_mode_changeable",
            "xml_name": "isEnergyModeChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "power",
            "xml_name": "power",
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
            "name": "is_power_changeable",
            "xml_name": "isPowerChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "energy",
            "xml_name": "energy",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "is_energy_changeable",
            "xml_name": "isEnergyChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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


@spine_type('ns_p:DirectControlDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class DirectControlDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_DirectControl.xsd:ns_p:DirectControlDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
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
    ]


@spine_type('ns_p:DirectControlDescriptionDataType', is_value_type=False, no_attrib_name=False)
class DirectControlDescriptionDataType(SpineBase): # EEBus_SPINE_TS_DirectControl.xsd:ns_p:DirectControlDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
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
    ]


@spine_type('ns_p:DirectControlActivityListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class DirectControlActivityListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_DirectControl.xsd:ns_p:DirectControlActivityListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
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


@spine_type('ns_p:DirectControlActivityListDataType', is_value_type=False, no_attrib_name=False)
class DirectControlActivityListDataType(SpineBase): # EEBus_SPINE_TS_DirectControl.xsd:ns_p:DirectControlActivityListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "direct_control_activity_data",
            "xml_name": "directControlActivityData",
            "type": "ns_p:DirectControlActivityDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "activity_state",
            "xml_name": "activityState",
            "type": "ns_p:DirectControlActivityStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlActivityStateType"
        },
        {
            "name": "is_activity_state_changeable",
            "xml_name": "isActivityStateChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "energy_mode",
            "xml_name": "energyMode",
            "type": "ns_p:EnergyModeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EnergyModeType"
        },
        {
            "name": "is_energy_mode_changeable",
            "xml_name": "isEnergyModeChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "power",
            "xml_name": "power",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "is_power_changeable",
            "xml_name": "isPowerChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "energy",
            "xml_name": "energy",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "is_energy_changeable",
            "xml_name": "isEnergyChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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


@spine_type('ns_p:DirectControlActivityDataElementsType', is_value_type=False, no_attrib_name=False)
class DirectControlActivityDataElementsType(SpineBase): # EEBus_SPINE_TS_DirectControl.xsd:ns_p:DirectControlActivityDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "activity_state",
            "xml_name": "activityState",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_activity_state_changeable",
            "xml_name": "isActivityStateChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "energy_mode",
            "xml_name": "energyMode",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_energy_mode_changeable",
            "xml_name": "isEnergyModeChangeable",
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
        {
            "name": "is_power_changeable",
            "xml_name": "isPowerChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "energy",
            "xml_name": "energy",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "is_energy_changeable",
            "xml_name": "isEnergyChangeable",
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

