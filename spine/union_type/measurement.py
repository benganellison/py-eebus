# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass



@spine_type('ns_p:MeasurementValueStateType', is_value_type=True, no_attrib_name=False)
class MeasurementValueStateType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementValueStateType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:MeasurementValueTendencyType', is_value_type=True, no_attrib_name=False)
class MeasurementValueTendencyType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementValueTendencyType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:MeasurementValueSourceType', is_value_type=True, no_attrib_name=False)
class MeasurementValueSourceType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementValueSourceType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:MeasurementValueTypeType', is_value_type=True, no_attrib_name=False)
class MeasurementValueTypeType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementValueTypeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:MeasurementTypeType', is_value_type=True, no_attrib_name=False)
class MeasurementTypeType(SpineBase): # EEBus_SPINE_TS_Measurement.xsd:ns_p:MeasurementTypeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]

