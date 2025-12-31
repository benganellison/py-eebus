import pytest
from unittest.mock import MagicMock, patch
import time

# Types
from spine.base_message import SpineMessage
from spine.base_type.datagram import DatagramType, HeaderType, PayloadType
from spine.base_type.commandframe import CmdType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.simple_type.commandframe import MsgCounterType
from spine.base_type.loadcontrol import (
    LoadControlLimitListDataType,
    LoadControlLimitDataType,
)
from spine.simple_type.loadcontrol import LoadControlLimitIdType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import NumberType, ScaleType

class MockActor:
    def __init__(self, name):
        self.name = name
        self.state = "INIT"
        self.last_heartbeat = 0
        self.active_power_limit = None
        
    def receive_heartbeat(self):
        self.last_heartbeat = time.time()
        
    def receive_limit(self, limit_value):
        # Transition to CONTROLLED if valid limit received
        self.active_power_limit = limit_value
        self.state = "CONTROLLED"

    def check_failsafe(self, timeout=1.0):
        # 1.0s timeout for test speed
        if time.time() - self.last_heartbeat > timeout:
            self.state = "FAILSAFE"

def test_lpc_state_machine_transitions():
    """
    Scenario: Verify transitions between INIT, CONTROLLED, and FAILSAFE states.
    
    Flow:
    1. Start in INIT.
    2. Energy Guard sends Limit -> CS transitions to CONTROLLED.
    3. Heartbeats stop -> CS transitions to FAILSAFE.
    """
    cs = MockActor("ControllableSystem")
    
    # 1. Initial State
    assert cs.state == "INIT"
    
    # 2. Receive Limit (Simulate "Write" command)
    # Constructing a valid limit object just to verify we can handle the type
    limit_value = ScaledNumberType(number=NumberType(value=1000), scale=ScaleType(value=0)) # 1000W
    
    cs.receive_limit(limit_value)
    assert cs.state == "CONTROLLED"
    assert cs.active_power_limit == limit_value
    
    # 3. Heartbeat Logic
    cs.receive_heartbeat()
    cs.check_failsafe(timeout=1.0)
    assert cs.state == "CONTROLLED" # Should still be controlled
    
    # 4. Simulate Timeout
    import time
    time.sleep(1.1) 
    cs.check_failsafe(timeout=1.0)
    assert cs.state == "FAILSAFE"
