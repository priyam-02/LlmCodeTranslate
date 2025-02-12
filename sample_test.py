import ollama

client = ollama.Client()


model = "llama3.1"
# Define the source code, source language, and target language
source_language = "C"
target_language = "Python"
source_code = """
#include <stdio.h>

int main(){
    char c;
 
    while(scanf("%c",&c)!=EOF){
         printf("%c",toupper(c));
    }
    return(0);
   
}
"""

# Create the translation prompt
prompt = f"""
You are a skilled software developer proficient in multiple programming languages. Your task is to accurately rewrite the following {source_language} code into {target_language} while preserving all functionality. The {target_language} program must meet the following criteria:

1. Functionality Preservation
•	Translate all functions, loops, conditions, and logic from C to Python exactly so that the behavior remains identical.
•	Ensure mathematical operations, data structures, and algorithm logic remain unchanged.
•	Do not modify the fundamental algorithm or introduce alternative methods unless explicitly required.

2. Logical Accuracy
•	Preserve the original logic for counting, summing, and assignments.
•	Maintain the same variable order in function parameters, assignments, and input handling.
•	Avoid modifying the sequence of operations, ensuring Python executes each step in the exact same order as C.
•	Do not impose uniqueness constraints or filters unless explicitly present in the C code. If C allows duplicates, Python must also.

3. Input Handling (Critical for Accurate Conversion)
    •	Ensure input reading follows the same structure as C’s scanf():
          o	If scanf() reads all input values in a single line, replicate this behavior in Python.
          o	If scanf() reads multiple lines, replicate the exact line-by-line reading process.
    •	Use sys.stdin.read() or sys.stdin.readline() instead of input() for batch processing.
    •	Preserve space-separated input reading, avoiding unnecessary use of splitlines().
    •	Ensure floating-point values are read correctly without truncation or type conversion errors.

4. Output Handling
    •	The Python output must match the C output exactly:
          o	Do not add extra spaces, newlines, or unnecessary print messages.
          o	Ensure conditional branches (if/else) preserve output logic precisely.

5. Memory Management & Data Structures
•	Convert fixed-size arrays in C to dynamic lists in Python only if needed.
•	Preserve array indexing logic, ensuring no off-by-one errors.

6. Error Handling & Edge Cases
    •	Preserve all C boundary conditions, including:
          o	Negative values, zero values, and large inputs.
          o	Division by zero, out-of-bounds errors, and incorrect input handling.
    •	Ensure invalid input is handled the same way as C:
          o	If scanf() in C stops reading on invalid input, Python should do the same.
          o	Avoid premature termination unless explicitly required.

7. Efficient & Idiomatic Python Code (without changing logic)
•	Use Python conventions where possible but do not change the algorithm.
•	Avoid unnecessary recursion if it might cause stack overflow; replace it with loops when needed.

8. Correct Import Usage
•	Import only necessary modules (e.g., sys, math).
•	Do not introduce unnecessary dependencies.

9. Strictly Maintain Sorting, Comparisons, and Assignments
•	Ensure all conditions (if, else if, else), comparisons (>=, >, <), and assignments are translated exactly.
•	Do not modify ranking logic, sorting behavior, or duplicate handling unless explicitly required.

10. Input Validation & Edge Cases
•	If scanf() in C checks for a specific number of inputs (e.g., == 8), Python must strictly enforce this check.
•	The Python code must skip invalid input cases just like C and should not assume inputs will always be correct.


Here is the C code that needs to be translated into Python:

{source_code}

Respond with Python output code only. Do not include explanations, comments, or additional formatting in your response. The output should be a fully executable Python program.
"""

try:
    # Generate a response from Ollama
    response = client.generate(model=model, prompt=prompt)
    translated_code = response["response"]
  
    print("Translated Code in Python:")
    print(translated_code)
except Exception as e:
    print("An error occurred:", e)
