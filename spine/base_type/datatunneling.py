# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.datatunneling import ChannelIdType
    from spine.simple_type.datatunneling import PurposeIdType



@spine_type('ns_p:DataTunnelingHeaderElementsType', is_value_type=False, no_attrib_name=False)
class DataTunnelingHeaderElementsType(SpineBase): # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:DataTunnelingHeaderElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "purpose_id",
            "xml_name": "purposeId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "channel_id",
            "xml_name": "channelId",
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


@spine_type('ns_p:DataTunnelingHeaderType', is_value_type=False, no_attrib_name=False)
class DataTunnelingHeaderType(SpineBase): # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:DataTunnelingHeaderType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "purpose_id",
            "xml_name": "purposeId",
            "type": "ns_p:PurposeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PurposeIdType"
        },
        {
            "name": "channel_id",
            "xml_name": "channelId",
            "type": "ns_p:ChannelIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ChannelIdType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:DataTunnelingCallElementsType', is_value_type=False, no_attrib_name=False)
class DataTunnelingCallElementsType(SpineBase): # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:DataTunnelingCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "header",
            "xml_name": "header",
            "type": "ns_p:DataTunnelingHeaderElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DataTunnelingHeaderElementsType"
        },
        {
            "name": "purpose_id",
            "xml_name": "purposeId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "channel_id",
            "xml_name": "channelId",
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
        {
            "name": "payload",
            "xml_name": "payload",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DataTunnelingCallType', is_value_type=False, no_attrib_name=False)
class DataTunnelingCallType(SpineBase): # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:DataTunnelingCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "header",
            "xml_name": "header",
            "type": "ns_p:DataTunnelingHeaderType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DataTunnelingHeaderType"
        },
        {
            "name": "purpose_id",
            "xml_name": "purposeId",
            "type": "ns_p:PurposeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PurposeIdType"
        },
        {
            "name": "channel_id",
            "xml_name": "channelId",
            "type": "ns_p:ChannelIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ChannelIdType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "payload",
            "xml_name": "payload",
            "type": "xs:hexBinary",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]

