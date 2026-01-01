from spine.base_type.datagram import DatagramType, PayloadType, HeaderType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.base_type.commondatatypes import FeatureAddressType
from spine.simple_type.commondatatypes import AddressDeviceType, AddressEntityType, AddressFeatureType, LabelType, DescriptionType, SpecificationVersionType
from spine.simple_type.commandframe import MsgCounterType
from spine.enums.commandframe import CmdClassifierType
from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueListDataType,
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueValueType
)
from spine.simple_type.deviceconfiguration import (
    DeviceConfigurationKeyIdType,
    DeviceConfigurationKeyValueStringType
)
from spine.union_type.deviceconfiguration import DeviceConfigurationKeyNameType

class TestDeviceConfiguration:
    def test_device_configuration_construction(self):
        # Create Device Configuration Data
        # Tests simple type aliases and nested choice types
        
        # Key ID is a simple aliased int
        key_id = DeviceConfigurationKeyIdType(value=1)
        
        # Value is a complex choice type
        # testing string value variant
        kv_value = DeviceConfigurationKeyValueValueType(
            string=DeviceConfigurationKeyValueStringType(value="Standby")
        )
        
        kv_data = DeviceConfigurationKeyValueDataType(
            key_id=key_id,
            value=kv_value,
            is_value_changeable=True
        )
        
        kv_list = DeviceConfigurationKeyValueListDataType(
            device_configuration_key_value_data=[kv_data]
        )
        
        data = kv_list.get_data()
        
        assert len(data["deviceConfigurationKeyValueData"]) == 1
        item = data["deviceConfigurationKeyValueData"][0]
        assert item["keyId"] == 1
        assert item["value"]["string"] == "Standby"
        assert item["isValueChangeable"] is True

    def test_device_configuration_full_serialization(self):
        # Verify full message nesting with PayloadContributionGroup
        
        # Construct a more complex value (e.g. boolean)
        kv_value_bool = DeviceConfigurationKeyValueValueType(
            boolean=True
        )
        
        kv_data = DeviceConfigurationKeyValueDataType(
            key_id=DeviceConfigurationKeyIdType(value=2),
            value=kv_value_bool,
            is_value_changeable=False
        )
        
        kv_list = DeviceConfigurationKeyValueListDataType(
            device_configuration_key_value_data=[kv_data]
        )

        cmd = CmdType(
            payload_contribution_group=PayloadContributionGroup(
                device_configuration_key_value_list_data=kv_list
            )
        )
        
        datagram = DatagramType(
            header=HeaderType(
                specification_version=SpecificationVersionType(value="1.3.0"),
                address_source=FeatureAddressType(
                    device=AddressDeviceType(value="d:_i:EMS"),
                    entity=[AddressEntityType(value=1)],
                    feature=AddressFeatureType(value=1)
                ),
                address_destination=FeatureAddressType(
                    entity=[AddressEntityType(value=0)],
                    feature=AddressFeatureType(value=0)
                ),
                msg_counter=MsgCounterType(value=2002),
                cmd_classifier=CmdClassifierType.read
            ),
            payload=PayloadType(cmd=[cmd])
        )
        
        serialized = datagram.get_data()
        
        cmd_data = serialized["payload"]["cmd"][0]
        
        assert "payload_contribution_group" in cmd_data
        group = cmd_data["payload_contribution_group"]
        assert "deviceConfigurationKeyValueListData" in group
        
        item = group["deviceConfigurationKeyValueListData"]["deviceConfigurationKeyValueData"][0]
        assert item["keyId"] == 2
        assert item["value"]["boolean"] is True
        assert item["isValueChangeable"] is False
