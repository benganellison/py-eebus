from spine.base_type.datagram import DatagramType, PayloadType, HeaderType
from spine.base_type.commandframe import CmdType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.simple_type.commondatatypes import AddressDeviceType, AddressEntityType, AddressFeatureType, LabelType, DescriptionType, SpecificationVersionType
from spine.simple_type.commandframe import MsgCounterType
from spine.enums.commandframe import CmdClassifierType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.base_type.deviceclassification import DeviceClassificationManufacturerDataType
from spine.simple_type.deviceclassification import DeviceClassificationStringType
from spine.union_type.deviceclassification import PowerSourceType

class TestDeviceClassification:
    def test_device_classification_construction(self):
        # Create a Device Classification Manufacturer Data structure
        # This tests basic object construction and the patches applied to UnionTypes (PowerSourceType)
        
        # PowerSourceType is a Union, expecting a string value now that it's patched
        power_source = PowerSourceType(value="mains")
        
        manufacturer_data = DeviceClassificationManufacturerDataType(
            device_name=DeviceClassificationStringType(value="MySmartDevice"),
            vendor_name=DeviceClassificationStringType(value="Acme Corp"),
            serial_number=DeviceClassificationStringType(value="SN-12345678"),
            power_source=power_source,
            manufacturer_node_identification=DeviceClassificationStringType(value="Node-001"),
            manufacturer_label=LabelType(value="Main Controller"),
            manufacturer_description=DescriptionType(value="Primary control unit for the house")
        )
        
        assert manufacturer_data.device_name.value == "MySmartDevice"
        assert manufacturer_data.power_source.value == "mains"
        
        # Verify serialization
        data = manufacturer_data.get_data()
        
        assert data["deviceName"] == "MySmartDevice"
        assert data["vendorName"] == "Acme Corp"
        assert data["powerSource"] == "mains" # This verifies the UnionType patch works
        assert data["manufacturerNodeIdentification"] == "Node-001"

    def test_device_classification_message_structure(self):
        # Verify full message nesting
        manufacturer_data = DeviceClassificationManufacturerDataType(
            device_name=DeviceClassificationStringType(value="HeatPump-XA1"),
            vendor_code=DeviceClassificationStringType(value="VC-99"),
            power_source=PowerSourceType(value="unknown") # Testing another enum/string value
        )
        
        cmd = CmdType(
            payload_contribution_group=PayloadContributionGroup(
                device_classification_manufacturer_data=manufacturer_data
            )
        )
        
        payload = PayloadType(cmd=[cmd])
        
        datagram = DatagramType(
            header=HeaderType(
                specification_version=SpecificationVersionType(value="1.3.0"),
                address_source=FeatureAddressType(
                    device=AddressDeviceType(value="d:_i:1234"),
                    entity=[AddressEntityType(value=1)],
                    feature=AddressFeatureType(value=1)
                ),
                address_destination=FeatureAddressType(
                    entity=[AddressEntityType(value=0)],
                    feature=AddressFeatureType(value=0)
                ),
                msg_counter=MsgCounterType(value=101),
                cmd_classifier=CmdClassifierType.read
            ),
            payload=payload
        )
        
        serialized = datagram.get_data()
        
        # Verify structure
        # Note: generated code keeps explicit nesting for groups
        cmd_data = serialized["payload"]["cmd"][0]
        assert "payload_contribution_group" in cmd_data
        assert cmd_data["payload_contribution_group"]["deviceClassificationManufacturerData"]["deviceName"] == "HeatPump-XA1"
        assert cmd_data["payload_contribution_group"]["deviceClassificationManufacturerData"]["powerSource"] == "unknown"
