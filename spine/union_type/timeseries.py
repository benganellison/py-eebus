# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:TimeSeriesTypeType', is_value_type=False, no_attrib_name=False)
class TimeSeriesTypeType(SpineBase): # EEBus_SPINE_TS_TimeSeries.xsd:ns_p:TimeSeriesTypeType -> UnionType
    _MEMBER_INFO = [
    ]

