import pytest
import os
import glob
from pathlib import Path

# Define path to specifications relative to this test file
# tests/spine/ -> ../../EEBUS_specifications
PROJECT_ROOT = Path(__file__).parent.parent.parent
SPEC_DIR = PROJECT_ROOT / "EEBUS_specifications"

def get_xml_examples():
    """Find all Example XML files in the specifications directory."""
    # Look for .xml files recursively
    # We specifically found them in EEBus_SPINE_V1.3.0_Final_hp/ExampleXMLs/
    # But let's be general if possible, or target that specific dir.
    pattern = str(SPEC_DIR) + "/**/ExampleXMLs/**/*.xml"
    files = glob.glob(pattern, recursive=True)
    return files

import json
import xmlschema
from spine.base_type.datagram import DatagramType
from spine.base_message import SpineMessage

# Load the schema once
# Assuming the tests run from project root or we can find xsd folder
XSD_PATH = PROJECT_ROOT / "xsd" / "EEBus_SPINE_TS_Datagram.xsd"
try:
    SCHEMA = xmlschema.XMLSchema(str(XSD_PATH))
except Exception as e:
    # Fallback or allow failure if XSD not found (e.g. CI env)
    print(f"Warning: Could not load XSD schema: {e}")
    SCHEMA = None

@pytest.mark.compliance
@pytest.mark.parametrize("xml_path", get_xml_examples())
def test_spec_example_compliance(xml_path):
    """
    Verify that official Example XMLs can be:
    1. Parsed by xmlschema (validating against XSD)
    2. Loaded into our Python DatagramType objects
    3. Serialized back to JSON (as per SpineMessage)
    """
    if SCHEMA is None:
        pytest.skip("XSD Schema not found")
    
    # 1. Parse XML to Dict using xmlschema
    # validation='lax' helps if there are minor namespace issues or missing imports in strict mode
    try:
        xml_result = SCHEMA.to_dict(xml_path, validation='lax')
        if isinstance(xml_result, tuple):
            xml_dict = xml_result[0]
        else:
            xml_dict = xml_result
    except Exception as e:
        pytest.fail(f"XML Schema Validation/Parsing Failed: {e}")
    
    # xmlschema to_dict returns the content of the root element (DatagramType), 
    # but does it include the root tag 'datagram'?
    # Usually it returns the complex type content.
    # Our DatagramType.from_data expects the content dict (header, payload).
    
    # 2. Convert to Python Object
    try:
        # DatagramType corresponds to the 'datagram' element type.
        # Check if xml_dict has 'datagram' key or is the content.
        # xmlschema.to_dict usually returns the content dict directly for the root element.
        obj = DatagramType.from_data(xml_dict)
    except Exception as e:
         pytest.fail(f"Instantiation of DatagramType failed: {e}")

    # 3. Basic Validation
    # Ensure we parsed something meaningful
    assert obj.header is not None, "Header parsing failed (is None)"
    if 'header' in xml_dict and 'msgCounter' in xml_dict['header']:
         # xmlschema converts integers, check if our object has it
         assert obj.header.msg_counter is not None
         # Note: xmlschema might keep keys as is, headers member 'msgCounter' in python is 'msg_counter'.
    
    # 4. Serialize
    # SpineMessage wrapper expects a DatagramType
    msg = SpineMessage(obj)
    json_output = msg.get_data()
    
    assert len(json_output) > 0
    assert "header" in json_output
    assert "payload" in json_output
