from spine.base_type.datagram import DatagramType, PayloadType, HeaderType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.base_type.commondatatypes import FeatureAddressType
from spine.simple_type.commondatatypes import AddressDeviceType, AddressEntityType, AddressFeatureType, LabelType, DescriptionType, SpecificationVersionType
from spine.simple_type.commandframe import MsgCounterType
from spine.enums.commandframe import CmdClassifierType
from spine.base_type.timeseries import TimeSeriesListDataType, TimeSeriesDataType, TimeSeriesSlotType
from spine.simple_type.timeseries import TimeSeriesIdType, TimeSeriesSlotIdType, TimeSeriesSlotCountType
from spine.union_type.timeseries import TimeSeriesTypeType
from spine.union_type.commondatatypes import ScopeTypeType

class TestTimeSeries:
    def test_timeseries_construction(self):
        # Create Time Series Data
        # Tests list handling, nested objects, and UnionTypes
        
        slot1 = TimeSeriesSlotType(
            time_series_slot_id=TimeSeriesSlotIdType(value=1),
            duration="PT1H", # xs:duration format
            value=None # Optional
        )
        
        ts_data = TimeSeriesDataType(
            time_series_id=TimeSeriesIdType(value=100),
            time_series_slot=[slot1]
        )
        
        ts_list = TimeSeriesListDataType(
            time_series_data=[ts_data]
        )
        
        data = ts_list.get_data()
        
        assert len(data["timeSeriesData"]) == 1
        assert data["timeSeriesData"][0]["timeSeriesId"] == 100
        assert data["timeSeriesData"][0]["timeSeriesSlot"][0]["duration"] == "PT1H"

    def test_timeseries_full_message_serialization(self):
        # Verify full message nesting with PayloadContributionGroup
        
        # TimeSeriesTypeType is a UnionType we patched
        ts_type = TimeSeriesTypeType(value="planning")
        
        ts_data = TimeSeriesDataType(
            time_series_id=TimeSeriesIdType(value=55),
            # Note: TimeSeriesTypeType isn't a direct member of TimeSeriesDataType in the spec I viewed earlier?
            # Let's check TimeSeriesDescriptionDataType if needed. 
            # Looking at my previous view_file of base_type/timeseries.py:
            # TimeSeriesDataType has: time_series_id, time_period, ... time_series_slot...
            # TimeSeriesDescriptionDataType has: time_series_id, time_series_type
            
            # Let's verify TimeSeriesDescriptionDataType usage too
        )
        
        # Testing description data to capture the UnionType patch usage
        from spine.base_type.timeseries import TimeSeriesDescriptionDataType, TimeSeriesDescriptionListDataType
        
        ts_desc = TimeSeriesDescriptionDataType(
            time_series_id=TimeSeriesIdType(value=55),
            time_series_type=TimeSeriesTypeType(value="planning"),
            label=LabelType(value="Generated Plan")
        )
        
        desc_list = TimeSeriesDescriptionListDataType(
            time_series_description_data=[ts_desc]
        )

        cmd = CmdType(
            payload_contribution_group=PayloadContributionGroup(
                time_series_description_list_data=desc_list
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
                msg_counter=MsgCounterType(value=1001),
                cmd_classifier=CmdClassifierType.notify
            ),
            payload=PayloadType(cmd=[cmd])
        )
        
        serialized = datagram.get_data()
        
        cmd_data = serialized["payload"]["cmd"][0]
        
        assert "payload_contribution_group" in cmd_data
        group = cmd_data["payload_contribution_group"]
        assert "timeSeriesDescriptionListData" in group
        
        item = group["timeSeriesDescriptionListData"]["timeSeriesDescriptionData"][0]
        assert item["timeSeriesId"] == 55
        assert item["timeSeriesType"] == "planning" # Verifies UnionType patch
        assert item["label"] == "Generated Plan"
