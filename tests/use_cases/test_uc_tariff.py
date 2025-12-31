import pytest
import json
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType
from spine.simple_type.commondatatypes import LabelType

from spine.base_type.tariffinformation import (
    TariffDescriptionDataType,
    TariffDescriptionListDataType,
    TariffDataType,
    TariffListDataType,
    TierDataType,
    TierDescriptionDataType,
    TierDescriptionListDataType
)
from spine.simple_type.tariffinformation import TariffIdType, TierIdType
from spine.union_type.commondatatypes import ScopeTypeType, CurrencyType
from spine.union_type.tariffinformation import TierTypeType

def test_tariff_structure():
    """
    Tariff Test: Verify construction of Tariff Information.
    Scenario: Define a basic ToU Tariff (Tariff ID 1).
    """
    
    # 1. Tariff Description
    # Using raw strings/integers where UnionTypes are involved if the union logic allows,
    # or specific UnionType wrappers if strict.
    # Previous tests showed UnionTypes need wrappers or specific values.
    
    tariff_desc = TariffDescriptionDataType(
        tariff_id=TariffIdType(value=1),
        scope_type=ScopeTypeType(value="timeOfUse"),
        tariff_writeable=False,
        update_required=False
    )
    
    tariff_desc_list = TariffDescriptionListDataType(
        tariff_description_data=[tariff_desc]
    )
    
    # 1b. Tier Description (New Optimization)
    tier_desc = TierDescriptionDataType(
        tier_id=TierIdType(value=1),
        tier_type=TierTypeType(value="timeOfUse"),
        label=LabelType(value="Peak Hour")
    )
    
    tier_desc_list = TierDescriptionListDataType(
        tier_description_data=[tier_desc]
    )
    
    # 2. Tariff Data (Active Tier)
    # Tier ID 1 is active
    # Tier ID 1 is active
    tariff_data = TariffDataType(
        tariff_id=TariffIdType(value=1),
        active_tier_id=[TierIdType(value=1)]
    )
    
    tariff_data_list = TariffListDataType(
        tariff_data=[tariff_data]
    )
    
    # 3. Construct Payload
    cmd_desc = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            tariff_description_list_data=tariff_desc_list,
            tier_description_list_data=tier_desc_list
        )
    )
    
    cmd_data = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            tariff_list_data=tariff_data_list
        )
    )
    
    datagram = DatagramType(
        header=HeaderType(
            msg_counter=MsgCounterType(value=1),
            msg_counter_reference=None,
            cmd_classifier=None
        ),
        payload=PayloadType(
            cmd=[cmd_desc, cmd_data]
        )
    )
    
    # 4. Serialization
    msg = SpineMessage(datagram)
    json_str = msg.get_data()
    data = json.loads(json_str)
    
    payload_cmds = data["datagram"]["payload"]["cmd"]
    
    # Verify Description
    # Note: CamelCase key 'tariffDescriptionListData' expected
    desc_payload = payload_cmds[0]["payload_contribution_group"]["tariffDescriptionListData"]["tariffDescriptionData"][0]
    assert desc_payload["tariffId"] == 1
    assert desc_payload["scopeType"] == "timeOfUse"
    
    # Verify Data
    data_payload = payload_cmds[1]["payload_contribution_group"]["tariffListData"]["tariffData"][0]
    assert data_payload["tariffId"] == 1
    assert data_payload["activeTierId"] == [1]

    # Verify Tier Description
    tier_payload = payload_cmds[0]["payload_contribution_group"]["tierDescriptionListData"]["tierDescriptionData"][0]
    assert tier_payload["tierId"] == 1
    assert tier_payload["tierType"] == "timeOfUse"
