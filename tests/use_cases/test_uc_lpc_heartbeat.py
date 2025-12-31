from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType

from spine.base_type.devicediagnosis import DeviceDiagnosisHeartbeatDataType

# Note: heartbeat_counter is defined as xs:unsignedLong -> int
# heartbeat_timeout is defined as xs:duration -> str

def test_lpc_heartbeat_construction():
    """
    Scenario 3: Heartbeat.
    Verify we can construct a DeviceDiagnosisHeartbeatDataType.
    """
    # Heartbeat Counter = 0, Timeout = 120s
    heartbeat_data = DeviceDiagnosisHeartbeatDataType(
        heartbeat_counter=0,
        heartbeat_timeout="PT120S"
    )

    assert heartbeat_data.heartbeat_counter == 0
    assert heartbeat_data.heartbeat_timeout == "PT120S"

    # Wrap in Datagram
    cmd = CmdType(
        payload_contribution_group=PayloadContributionGroup(
            device_diagnosis_heartbeat_data=heartbeat_data
        )
    )

    datagram = DatagramType(
        header=HeaderType(
            msg_counter=MsgCounterType(value=1),
            msg_counter_reference=None,
            cmd_classifier=None
        ),
        payload=PayloadType(
            cmd=[cmd]
        )
    )
    
    # Verify serialization structure
    msg = SpineMessage(datagram)
    import json
    json_output = json.loads(msg.get_data())
    
    payload = json_output["datagram"]["payload"]["cmd"][0]
    # Check that the heartbeat data is present
    heartbeat_json = payload["payload_contribution_group"]["deviceDiagnosisHeartbeatData"]
    assert heartbeat_json["heartbeatCounter"] == 0
    assert heartbeat_json["heartbeatTimeout"] == "PT120S"
