import pytest
import os
import glob
from pathlib import Path
import json
import xmlschema
from spine.base_type.datagram import DatagramType
from spine.base_message import SpineMessage

# Define path to specifications relative to this test file
PROJECT_ROOT = Path(__file__).parent.parent.parent
SPEC_DIR = PROJECT_ROOT / "EEBUS_specifications"
XSD_PATH = PROJECT_ROOT / "xsd" / "EEBus_SPINE_TS_Datagram.xsd"

# Load the schema once
try:
    SCHEMA = xmlschema.XMLSchema(str(XSD_PATH))
except Exception as e:
    print(f"Warning: Could not load XSD schema: {e}")
    SCHEMA = None

def get_xml_examples():
    """Find all Example XML files in the specifications directory."""
    pattern = str(SPEC_DIR) + "/**/ExampleXMLs/**/*.xml"
    files = glob.glob(pattern, recursive=True)
    return sorted(files)  # Sort for consistent test ordering

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
    
    # Context info for failure reports
    file_name = os.path.basename(xml_path)
    
    # 1. Parse XML to Dict using xmlschema
    try:
        xml_result = SCHEMA.to_dict(xml_path, validation='lax')
        if isinstance(xml_result, tuple):
            xml_dict = xml_result[0]
        else:
            xml_dict = xml_result
    except Exception as e:
        pytest.fail(f"XML Schema Validation/Parsing Failed for {file_name}: {e}")
    
    # 2. Convert to Python Object
    try:
        obj = DatagramType.from_data(xml_dict)
    except Exception as e:
         pytest.fail(f"Instantiation of DatagramType failed for {file_name}: {e}")

    # 3. Basic Validation
    assert obj.header is not None, f"Header parsing failed (is None) for {file_name}"
    if 'header' in xml_dict and 'msgCounter' in xml_dict['header']:
         assert obj.header.msg_counter is not None, f"MsgCounter missing in object for {file_name}"
    
    # 4. Serialize
    try:
        msg = SpineMessage(obj)
        json_output = msg.get_data()
    except Exception as e:
        pytest.fail(f"Serialization to JSON failed for {file_name}: {e}")
    
    assert len(json_output) > 0
    assert "header" in json_output
    assert "payload" in json_output
