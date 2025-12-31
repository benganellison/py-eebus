import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.measurement import (
    MeasurementDataType,
    MeasurementListDataType,
    MeasurementDescriptionDataType,
    MeasurementDescriptionListDataType,
)
from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.measurement import MeasurementTypeType, MeasurementValueTypeType
from spine.union_type.commondatatypes import (
    CommodityTypeType,
    UnitOfMeasurementType,
    ScopeTypeType,
)
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import NumberType, ScaleType

def test_mpc_measurement_structure():
    """
    MPC Scenario: Energy Guard monitors Power Consumption.
    1. Define Measurement Description (ID 0: AC Power, Watts, Total Consumption)
    2. Define Measurement Value (ID 0: 5000 W)
    """
    
    # 1. Measurement Description
    desc_power = MeasurementDescriptionDataType(
        measurement_id=MeasurementIdType(value=0),
        measurement_type=MeasurementTypeType(value="power"),
        commodity_type=CommodityTypeType(value="electricity"),
        unit=UnitOfMeasurementType(value="W"),
        scope_type=ScopeTypeType(value="ACPowerTotal")
    )
    
    desc_list = MeasurementDescriptionListDataType(
        measurement_description_data=[desc_power]
    )
    
    # 2. Measurement Data (Positive = Consumption)
    val_power = MeasurementDataType(
        measurement_id=MeasurementIdType(value=0),
        value_type=MeasurementValueTypeType(value="value"),
        value=ScaledNumberType(
            number=NumberType(value=5000),
            scale=ScaleType(value=0)
        )
    )
    
    # Note: MeasurementListDataType usually wraps MeasurementDataType items
    # Checking if `MeasurementListDataType` exists in `base_type` or needs to be constructed
    meas_list = MeasurementListDataType(
        measurement_data=[val_power]
    )
    
    # 3. Construct Datagram
    cmd_desc = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            measurement_description_list_data=desc_list
        )
    )
    
    cmd_val = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            measurement_list_data=meas_list
        )
    )
    
    datagram = DatagramType(
        header=HeaderType(
            msg_counter=MsgCounterType(value=1),
            msg_counter_reference=None,
            cmd_classifier=None
        ),
        payload=PayloadType(
            cmd=[cmd_desc, cmd_val]
        )
    )
    
    # 4. Serialization
    msg = SpineMessage(datagram)
    json_str = msg.get_data()
    data = json.loads(json_str)
    
    payload_cmds = data["datagram"]["payload"]["cmd"]
    
    # Verify Description
    desc_payload = payload_cmds[0]["payload_contribution_group"]["measurementDescriptionListData"]["measurementDescriptionData"][0]
    assert desc_payload["measurementId"] == 0
    assert desc_payload["measurementType"] == "power"
    assert desc_payload["unit"] == "W"
    
    # Verify Value
    val_payload = payload_cmds[1]["payload_contribution_group"]["measurementListData"]["measurementData"][0]
    assert val_payload["measurementId"] == 0
    assert val_payload["value"]["number"] == 5000
