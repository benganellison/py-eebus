# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.simple_type.commondatatypes import SpecificationVersionType



@spine_type('ns_p:SpecificationVersionDataType', is_value_type=False, no_attrib_name=False)
class SpecificationVersionDataType(SpineBase): # EEBus_SPINE_TS_Version.xsd:ns_p:SpecificationVersionDataType -> ComplexType
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


@spine_type('ns_p:SpecificationVersionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SpecificationVersionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Version.xsd:ns_p:SpecificationVersionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:SpecificationVersionListDataType', is_value_type=False, no_attrib_name=False)
class SpecificationVersionListDataType(SpineBase): # EEBus_SPINE_TS_Version.xsd:ns_p:SpecificationVersionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "specification_version_data",
            "xml_name": "specificationVersionData",
            "type": "ns_p:SpecificationVersionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:SpecificationVersionDataElementsType', is_value_type=False, no_attrib_name=False)
class SpecificationVersionDataElementsType(SpineBase): # EEBus_SPINE_TS_Version.xsd:ns_p:SpecificationVersionDataElementsType -> ComplexType
    _MEMBER_INFO = [
    ]

