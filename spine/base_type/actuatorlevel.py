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
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.union_type.actuatorlevel import ActuatorLevelFctType
    from spine.union_type.commondatatypes import UnitOfMeasurementType



@spine_type('ns_p:ActuatorLevelDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class ActuatorLevelDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_ActuatorLevel.xsd:ns_p:ActuatorLevelDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
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
            "name": "level_default_unit",
            "xml_name": "levelDefaultUnit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:ActuatorLevelDescriptionDataType', is_value_type=False, no_attrib_name=False)
class ActuatorLevelDescriptionDataType(SpineBase): # EEBus_SPINE_TS_ActuatorLevel.xsd:ns_p:ActuatorLevelDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
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
            "name": "level_default_unit",
            "xml_name": "levelDefaultUnit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
    ]


@spine_type('ns_p:ActuatorLevelDataElementsType', is_value_type=False, no_attrib_name=False)
class ActuatorLevelDataElementsType(SpineBase): # EEBus_SPINE_TS_ActuatorLevel.xsd:ns_p:ActuatorLevelDataElementsType -> ComplexType
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


@spine_type('ns_p:ActuatorLevelDataType', is_value_type=False, no_attrib_name=False)
class ActuatorLevelDataType(SpineBase): # EEBus_SPINE_TS_ActuatorLevel.xsd:ns_p:ActuatorLevelDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:ActuatorLevelFctType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorLevelFctType"
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

