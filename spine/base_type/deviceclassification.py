# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.deviceclassification import DeviceClassificationStringType
    from spine.union_type.deviceclassification import PowerSourceType



@spine_type('ns_p:DeviceClassificationUserDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceClassificationUserDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationUserDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "user_node_identification",
            "xml_name": "userNodeIdentification",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "user_label",
            "xml_name": "userLabel",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "user_description",
            "xml_name": "userDescription",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceClassificationUserDataType', is_value_type=False, no_attrib_name=False)
class DeviceClassificationUserDataType(SpineBase): # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationUserDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "user_node_identification",
            "xml_name": "userNodeIdentification",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "user_label",
            "xml_name": "userLabel",
            "type": "ns_p:LabelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LabelType"
        },
        {
            "name": "user_description",
            "xml_name": "userDescription",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]


@spine_type('ns_p:DeviceClassificationManufacturerDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceClassificationManufacturerDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationManufacturerDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_name",
            "xml_name": "deviceName",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "device_code",
            "xml_name": "deviceCode",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "serial_number",
            "xml_name": "serialNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "software_revision",
            "xml_name": "softwareRevision",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "hardware_revision",
            "xml_name": "hardwareRevision",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "vendor_name",
            "xml_name": "vendorName",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "vendor_code",
            "xml_name": "vendorCode",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "brand_name",
            "xml_name": "brandName",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "power_source",
            "xml_name": "powerSource",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "manufacturer_node_identification",
            "xml_name": "manufacturerNodeIdentification",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "manufacturer_label",
            "xml_name": "manufacturerLabel",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "manufacturer_description",
            "xml_name": "manufacturerDescription",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceClassificationManufacturerDataType', is_value_type=False, no_attrib_name=False)
class DeviceClassificationManufacturerDataType(SpineBase): # EEBus_SPINE_TS_DeviceClassification.xsd:ns_p:DeviceClassificationManufacturerDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_name",
            "xml_name": "deviceName",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "device_code",
            "xml_name": "deviceCode",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "serial_number",
            "xml_name": "serialNumber",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "software_revision",
            "xml_name": "softwareRevision",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "hardware_revision",
            "xml_name": "hardwareRevision",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "vendor_name",
            "xml_name": "vendorName",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "vendor_code",
            "xml_name": "vendorCode",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "brand_name",
            "xml_name": "brandName",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "power_source",
            "xml_name": "powerSource",
            "type": "ns_p:PowerSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSourceType"
        },
        {
            "name": "manufacturer_node_identification",
            "xml_name": "manufacturerNodeIdentification",
            "type": "ns_p:DeviceClassificationStringType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationStringType"
        },
        {
            "name": "manufacturer_label",
            "xml_name": "manufacturerLabel",
            "type": "ns_p:LabelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LabelType"
        },
        {
            "name": "manufacturer_description",
            "xml_name": "manufacturerDescription",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]

