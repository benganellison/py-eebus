# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.enums.deviceconfiguration import DeviceConfigurationKeyValueTypeType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.deviceconfiguration import DeviceConfigurationKeyIdType
    from spine.simple_type.deviceconfiguration import DeviceConfigurationKeyValueStringType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.deviceconfiguration import DeviceConfigurationKeyNameType



@spine_type('ns_p:DeviceConfigurationKeyValueValueType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueValueType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueValueType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boolean",
            "xml_name": "boolean",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "date",
            "xml_name": "date",
            "type": "xs:date",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "string",
            "xml_name": "string",
            "type": "ns_p:DeviceConfigurationKeyValueStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueStringType"
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
            "name": "scaled_number",
            "xml_name": "scaledNumber",
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
            "name": "integer",
            "xml_name": "integer",
            "type": "xs:long",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueConstraintsDataType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueConstraintsDataType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "value_range_min",
            "xml_name": "valueRangeMin",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
        {
            "name": "boolean",
            "xml_name": "boolean",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "date",
            "xml_name": "date",
            "type": "xs:date",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "string",
            "xml_name": "string",
            "type": "ns_p:DeviceConfigurationKeyValueStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueStringType"
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
            "name": "scaled_number",
            "xml_name": "scaledNumber",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "integer",
            "xml_name": "integer",
            "type": "xs:long",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "value_range_max",
            "xml_name": "valueRangeMax",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
        {
            "name": "value_step_size",
            "xml_name": "valueStepSize",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueValueElementsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueValueElementsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueValueElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "boolean",
            "xml_name": "boolean",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "date",
            "xml_name": "date",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "string",
            "xml_name": "string",
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
            "name": "scaled_number",
            "xml_name": "scaledNumber",
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


@spine_type('ns_p:DeviceConfigurationKeyValueDescriptionDataType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueDescriptionDataType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "key_name",
            "xml_name": "keyName",
            "type": "ns_p:DeviceConfigurationKeyNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyNameType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:DeviceConfigurationKeyValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueTypeType"
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


@spine_type('ns_p:DeviceConfigurationKeyValueDataType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueDataType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
        {
            "name": "boolean",
            "xml_name": "boolean",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "date",
            "xml_name": "date",
            "type": "xs:date",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "string",
            "xml_name": "string",
            "type": "ns_p:DeviceConfigurationKeyValueStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueStringType"
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
            "name": "scaled_number",
            "xml_name": "scaledNumber",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "integer",
            "xml_name": "integer",
            "type": "xs:long",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "is_value_changeable",
            "xml_name": "isValueChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_configuration_key_value_constraints_data",
            "xml_name": "deviceConfigurationKeyValueConstraintsData",
            "type": "ns_p:DeviceConfigurationKeyValueConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "value_range_min",
            "xml_name": "valueRangeMin",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
        {
            "name": "value_range_max",
            "xml_name": "valueRangeMax",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
        {
            "name": "value_step_size",
            "xml_name": "valueStepSize",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_range_min",
            "xml_name": "valueRangeMin",
            "type": "ns_p:DeviceConfigurationKeyValueValueElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueElementsType"
        },
        {
            "name": "boolean",
            "xml_name": "boolean",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "date",
            "xml_name": "date",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "string",
            "xml_name": "string",
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
            "name": "scaled_number",
            "xml_name": "scaledNumber",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "value_range_max",
            "xml_name": "valueRangeMax",
            "type": "ns_p:DeviceConfigurationKeyValueValueElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueElementsType"
        },
        {
            "name": "value_step_size",
            "xml_name": "valueStepSize",
            "type": "ns_p:DeviceConfigurationKeyValueValueElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueElementsType"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "key_name",
            "xml_name": "keyName",
            "type": "ns_p:DeviceConfigurationKeyNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyNameType"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_configuration_key_value_description_data",
            "xml_name": "deviceConfigurationKeyValueDescriptionData",
            "type": "ns_p:DeviceConfigurationKeyValueDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "key_name",
            "xml_name": "keyName",
            "type": "ns_p:DeviceConfigurationKeyNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyNameType"
        },
        {
            "name": "value_type",
            "xml_name": "valueType",
            "type": "ns_p:DeviceConfigurationKeyValueTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueTypeType"
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


@spine_type('ns_p:DeviceConfigurationKeyValueDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "key_name",
            "xml_name": "keyName",
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


@spine_type('ns_p:DeviceConfigurationKeyValueListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueListDataType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueListDataType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_configuration_key_value_data",
            "xml_name": "deviceConfigurationKeyValueData",
            "type": "ns_p:DeviceConfigurationKeyValueDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:DeviceConfigurationKeyIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyIdType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:DeviceConfigurationKeyValueValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueType"
        },
        {
            "name": "is_value_changeable",
            "xml_name": "isValueChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:DeviceConfigurationKeyValueDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceConfigurationKeyValueDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "key_id",
            "xml_name": "keyId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:DeviceConfigurationKeyValueValueElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueValueElementsType"
        },
        {
            "name": "boolean",
            "xml_name": "boolean",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "date",
            "xml_name": "date",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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
            "name": "duration",
            "xml_name": "duration",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "string",
            "xml_name": "string",
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
            "name": "scaled_number",
            "xml_name": "scaledNumber",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "is_value_changeable",
            "xml_name": "isValueChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

