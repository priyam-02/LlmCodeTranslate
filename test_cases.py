# import subprocess
# import os

# # File mappings (Input and Expected Output)
# test_cases = [
#     ("in_1.txt", "out_1.txt")
# ]

# # Paths to files
# input_dir = "/Users/priyamshah/Documents/Individual Study/CodeNet88Samples/tests/p00003/"  # Update this if files are in a different directory
# translated_python_file = "translated_code.py"  # Save the translated Python code to this file

# # Execute the Python code with input and check against expected output
# def run_test_case(input_file, output_file):
#     with open(os.path.join(input_dir, input_file), "r") as infile:
#         input_data = infile.read()

#     expected_output_path = os.path.join(input_dir, output_file)
#     with open(expected_output_path, "r") as outfile:
#         expected_output = outfile.read().strip()

#     try:
#         # Execute the translated Python script
#         process = subprocess.run(
#             ["python3", translated_python_file],
#             input=input_data,
#             text=True,
#             capture_output=True,
#             check=True
#         )
#         actual_output = process.stdout.strip()
#         return actual_output == expected_output, actual_output, expected_output
#     except subprocess.CalledProcessError as e:
#         print(f"Execution failed: {e}")
#         return False, None, None

# # Main testing routine
# if __name__ == "__main__":
#     for input_file, output_file in test_cases:
#         result, actual, expected = run_test_case(input_file, output_file)
#         if result:
#             print(f"Test case {input_file} passed.")
#         else:
#             print(f"Test case {input_file} failed.")
#             print(f"Expected: {expected}")
#             print(f"Got: {actual}")

import subprocess
from pathlib import Path

# Directory paths
input_dir = Path("/Users/priyamshah/Documents/Individual Study/CodeNet88Samples/tests/p00020/")
translated_python_file = "translated_code.py"  # Save the translated Python code here

# Automatically discover input-output file pairs
test_cases = [(file, file.with_name(file.stem.replace("in", "out") + file.suffix))
              for file in input_dir.glob("in_*.txt")]

# Execute the Python code with input and check against expected output
def run_test_case(input_file, output_file):
    with input_file.open("r") as infile:
        input_data = infile.read()

    with output_file.open("r") as outfile:
        expected_output = outfile.read().strip()

    try:
        # Execute the translated Python script
        process = subprocess.run(
            ["python3", translated_python_file],
            input=input_data,
            text=True,
            capture_output=True,
            check=True
        )
        actual_output = process.stdout.strip()
        return actual_output == expected_output, actual_output, expected_output
    except subprocess.CalledProcessError as e:
        print(f"Execution failed: {e}")
        return False, None, None

# Main testing routine
if __name__ == "__main__":
    for input_file, output_file in test_cases:
        print(f"Running test case: {input_file.name}")
        if not output_file.exists():
            print(f"Missing expected output file for: {input_file.name}")
            continue
        
        result, actual, expected = run_test_case(input_file, output_file)
        if result:
            print(f"Test case {input_file.name} passed.")
        else:
            print(f"Test case {input_file.name} failed.")
            print(f"Expected:\n{expected}")
            print(f"Got:\n{actual}")