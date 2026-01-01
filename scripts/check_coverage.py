import re
import os
import argparse

def check_coverage(matrix_file, test_dir):
    """
    Checks which requirements in the matrix are covered by tests with @pytest.mark.requirement.
    Updates the matrix file with the results.
    """
    if not os.path.exists(matrix_file):
        print(f"Error: Matrix file {matrix_file} not found.")
        return

    # 1. Scan tests for markers
    # We look for @pytest.mark.requirement("LPC-TS-xxx")
    covered_reqs = {} # {req_id: [test_files]}
    
    print(f"Scanning tests in {test_dir}...")
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(".py") and file.startswith("test_"):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, start=os.getcwd())
                
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Regex for the marker
                # Matches: @pytest.mark.requirement("LPC-TS-001") or generic IDs
                matches = re.findall(r'@pytest\.mark\.requirement\s*\(\s*["\']([A-Z]+(?:-[A-Z]+)*-[0-9/]+)["\']', content)
                
                for req_id in matches:
                    if req_id not in covered_reqs:
                        covered_reqs[req_id] = set()
                    covered_reqs[req_id].add(rel_path)

    # 2. Update Matrix
    print("Updating matrix...")
    with open(matrix_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    header_processed = False
    
    # Regex to parse the table row: | ID | Desc | Status | Impl |
    row_pattern = re.compile(r'^\|\s*([A-Z]+(?:-[A-Z]+)*-[0-9/]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$')

    covered_count = 0
    total_count = 0

    for line in lines:
        match = row_pattern.match(line.strip())
        if match:
            total_count += 1
            req_id = match.group(1)
            desc = match.group(2)
            # preserve existing status if valid, but we are overwriting for now to be authoritative
            
            if req_id in covered_reqs:
                status = "Covered"
                impl = ", ".join(sorted(covered_reqs[req_id]))
                covered_count += 1
            else:
                status = "Pending"
                impl = ""
            
            new_lines.append(f"| {req_id} | {desc} | {status} | {impl} |\n")
        else:
            new_lines.append(line)

    with open(matrix_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Coverage: {covered_count}/{total_count} ({covered_count/total_count*100:.1f}%)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check LPC requirement coverage.")
    parser.add_argument("--matrix", default="docs/EEBUS_LPC_Traceability_Matrix.md", help="Path to matrix file.")
    parser.add_argument("--tests", default="tests", help="Directory to scan for tests.")
    
    args = parser.parse_args()
    
    check_coverage(args.matrix, args.tests)
