# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass


@spine_type('ns_p:TimeSeriesSlotIdType', is_value_type=True, no_attrib_name=False)
class TimeSeriesSlotIdType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesSlotIdType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:TimeSeriesSlotCountType', is_value_type=True, no_attrib_name=False)
class TimeSeriesSlotCountType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesSlotCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:TimeSeriesSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesSlotIdType"
        },
    ]


@spine_type('ns_p:TimeSeriesIdType', is_value_type=True, no_attrib_name=False)
class TimeSeriesIdType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesIdType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]

