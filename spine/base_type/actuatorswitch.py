# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.union_type.actuatorswitch import ActuatorSwitchFctType



@spine_type('ns_p:ActuatorSwitchDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class ActuatorSwitchDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDescriptionDataElementsType -> ComplexType
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
    ]


@spine_type('ns_p:ActuatorSwitchDescriptionDataType', is_value_type=False, no_attrib_name=False)
class ActuatorSwitchDescriptionDataType(SpineBase): # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDescriptionDataType -> ComplexType
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
    ]


@spine_type('ns_p:ActuatorSwitchDataElementsType', is_value_type=False, no_attrib_name=False)
class ActuatorSwitchDataElementsType(SpineBase): # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:ActuatorSwitchDataType', is_value_type=False, no_attrib_name=False)
class ActuatorSwitchDataType(SpineBase): # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:ActuatorSwitchFctType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorSwitchFctType"
        },
    ]

