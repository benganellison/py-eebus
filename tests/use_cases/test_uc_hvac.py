from spine.base_type.datagram import DatagramType, PayloadType, HeaderType
from spine.base_type.commandframe import CmdType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commondatatypes import AddressDeviceType, AddressEntityType, AddressFeatureType, LabelType, DescriptionType, SpecificationVersionType
from spine.simple_type.commandframe import MsgCounterType
from spine.enums.commandframe import CmdClassifierType
from spine.base_type.hvac import HvacOverrunDescriptionListDataType, HvacOverrunDescriptionDataType
from spine.simple_type.hvac import HvacOverrunIdType, HvacSystemFunctionIdType
from spine.union_type.hvac import HvacOverrunTypeType, HvacSystemFunctionTypeType

class TestHvac:
    def test_hvac_overrun_description_list_construction(self):
        # Create an HVAC Overrun Description List
        # Tests list handling and nested UnionTypes
        
        overrun1 = HvacOverrunDescriptionDataType(
            overrun_id=HvacOverrunIdType(value=1),
            overrun_type=HvacOverrunTypeType(value="temporary"), # UnionType patch check
            affected_system_function_id=[HvacSystemFunctionIdType(value=10)],
            label=LabelType(value="Boost Mode"),
            description=DescriptionType(value="Temporary boost for 1 hour")
        )
        
        overrun2 = HvacOverrunDescriptionDataType(
            overrun_id=HvacOverrunIdType(value=2),
            overrun_type=HvacOverrunTypeType(value="permanent"),
            label=LabelType(value="Holiday Mode")
        )
        
        overrun_list = HvacOverrunDescriptionListDataType(
            hvac_overrun_description_data=[overrun1, overrun2]
        )
        
        data = overrun_list.get_data()
        
        # Verify list serialization
        assert len(data["hvacOverrunDescriptionData"]) == 2
        assert data["hvacOverrunDescriptionData"][0]["overrunId"] == 1
        assert data["hvacOverrunDescriptionData"][0]["overrunType"] == "temporary" # Verify correct value serialization
        assert data["hvacOverrunDescriptionData"][1]["overrunType"] == "permanent"
        assert data["hvacOverrunDescriptionData"][0]["label"] == "Boost Mode"

    def test_hvac_full_message_serialization(self):
        # Verify wrapping in a full Datagram
        
        # Construct specific system function mapping
        # HvacSystemFunctionTypeType is also a UnionType needing the patch
        
        # Note: Importing HvacSystemFunctionTypeType from union_type
        
        overrun_list = HvacOverrunDescriptionListDataType(
            hvac_overrun_description_data=[
                HvacOverrunDescriptionDataType(
                    overrun_id=HvacOverrunIdType(value=99),
                    overrun_type=HvacOverrunTypeType(value="gridSignal"),
                    label=LabelType(value="Grid Critical Peak")
                )
            ]
        )

        cmd = CmdType(
            payload_contribution_group=PayloadContributionGroup(
                hvac_overrun_description_list_data=overrun_list
            )
        )
        
        datagram = DatagramType(
            header=HeaderType(
                specification_version=SpecificationVersionType(value="1.3.0"),
                address_source=FeatureAddressType(
                    device=AddressDeviceType(value="d:_i:HVAC_Sub"),
                    entity=[AddressEntityType(value=1)],
                    feature=AddressFeatureType(value=2)
                ),
                address_destination=FeatureAddressType(
                    entity=[AddressEntityType(value=0)],
                    feature=AddressFeatureType(value=0)
                ),
                msg_counter=MsgCounterType(value=255),
                cmd_classifier=CmdClassifierType.notify
            ),
            payload=PayloadType(cmd=[cmd])
        )
        
        serialized = datagram.get_data()
    
        cmd_data = serialized["payload"]["cmd"][0]
        assert "payload_contribution_group" in cmd_data
        assert "hvacOverrunDescriptionListData" in cmd_data["payload_contribution_group"]
        
        overrun_data = cmd_data["payload_contribution_group"]["hvacOverrunDescriptionListData"]["hvacOverrunDescriptionData"][0]
        
        assert overrun_data["overrunId"] == 99
        assert overrun_data["overrunType"] == "gridSignal"
        assert overrun_data["label"] == "Grid Critical Peak"
