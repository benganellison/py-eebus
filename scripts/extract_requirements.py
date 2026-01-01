import re
import os
import argparse

def extract_requirements(file_path):
    """
    Extracts requirements in the format [LPC-TS-xxx] from a markdown file.
    Returns a list of tuples (req_id, description_snippet).
    """
    requirements = []
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Regex to capture [LPC-TS-xxx] or [LPC-TS-xxx/y]
    # It might appear at the start of a line or inside text.
    # We'll look for lines starting with it or containing it prominently.
    # Based on the file view, it looks like: "[LPC-TS-001] The APCL SHALL..."
    
    # Regex to capture [PREFIX-Number] or [PREFIX-TS-Number] or variations
    # Examples: [LPC-TS-001], [CEVC-001], [LPC-TS-001/1]
    # We enforce a dash before the number to avoid matching things like [LPC1.0.0]
    req_pattern = re.compile(r'\[([A-Z]+(?:-[A-Z]+)*-[0-9]+(?:/[0-9]+)?)\]\s*(.*)')

    for line in lines:
        line = line.strip()
        match = req_pattern.search(line)
        if match:
            req_id = match.group(1)
            # The description might be cut off or continue, but we'll take the rest of the line as a snippet
            desc = match.group(2).strip()
            requirements.append((req_id, desc))
            
    return requirements

def generate_matrix(requirements, output_path):
    """
    Generates a Markdown table for the traceability matrix.
    """
    # Deduplicate by keeping the entry with the longest description
    unique_reqs = {}
    for req_id, desc in requirements:
        if req_id not in unique_reqs:
            unique_reqs[req_id] = desc
        else:
            if len(desc) > len(unique_reqs[req_id]):
                unique_reqs[req_id] = desc

    # Sort by ID
    sorted_reqs = sorted(unique_reqs.items())

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# EEBUS LPC Traceability Matrix\n\n")
        f.write("| Requirement ID | Description Snippet | Test Status | Implemented In |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        for req_id, desc in sorted_reqs:
            # Escape pipes
            safe_desc = desc.replace("|", "\|")
            # If description is too short/looks like junk, maybe warn? But longest logic helps.
            f.write(f"| {req_id} | {safe_desc} | Pending | | \n")
            
    print(f"Generated {output_path} with {len(sorted_reqs)} unique requirements.")

def process_path(path):
    """
    Recursively finds all .md files in a path and extracts requirements.
    """
    all_reqs = []
    
    if os.path.isfile(path):
        print(f"Processing file: {path}")
        return extract_requirements(path)
    
    if os.path.isdir(path):
        print(f"Scanning directory: {path}")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    # print(f"Processing: {file}")
                    all_reqs.extend(extract_requirements(full_path))
    return all_reqs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract EEBUS requirements from markdown specs.")
    parser.add_argument("input_path", help="Path to a specification file or directory containing .md files.")
    parser.add_argument("--output", default="docs/EEBUS_Traceability_Matrix.md", help="Output matrix file.")
    
    args = parser.parse_args()
    
    reqs = process_path(args.input_path)
    
    if reqs:
        generate_matrix(reqs, args.output)
    else:
        print("No requirements found.")
