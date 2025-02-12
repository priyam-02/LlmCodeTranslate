import ollama

client = ollama.Client()


model = "codellama"
# Define the source code, source language, and target language
source_language = "C"
target_language = "Python"
source_code = """
#include <stdio.h>

int main(void)
{
    int cars[10];

    int in_car;
    int cnt = 0;
    while (scanf("%d", &in_car) != EOF) {
        if (in_car != 0) {
            cars[cnt] = in_car;
            cnt++;
        } else {
            cnt--;
            printf("%d\n", cars[cnt]);
        }
    }

    return 0;
}
"""

# Create the translation prompt
prompt = f"""
You are a skilled software developer proficient in multiple programming languages. Your task is to accurately rewrite the following {source_language} code into {target_language} while preserving all functionality. The {target_language} program must meet the following criteria:

1️. Functionality Preservation
• Translate all logic exactly so that behavior remains identical.
• Preserve loop structures unless absolutely necessary to change.
• Ensure math operations, data structures, and algorithms remain identical.

2️. Correct Handling of Mutable vs Immutable Types
• If {target_language} has immutable equivalents (e.g., strings, tuples), functions must return new values instead of modifying in place.
• If {target_language} has mutable equivalents (lists, dicts, sets), modifications can be done in place.
• For arrays in C that are modified in place, use lists in Python only if needed.

3️. Strict Function Translation
• If a function modifies an argument in {source_language}, it must return the modified value in {target_language}.
• Do not assume direct modification works unless explicitly possible in {target_language}.
• Preserve return values to ensure correct updates.

4️. Avoid Overcomplication
• Do not replace simple loops with iterators or generators unless absolutely required.
• Do not use list comprehensions where a simple loop exists in {source_language}.
• Preserve step-by-step transformations from {source_language} to {target_language}.

5️. Input Handling Must Match {source_language}
• Use sys.stdin.readline() for line-based input.
• Use sys.stdin.read() for batch input processing.
• Preserve input structure (e.g., space-separated input should not be split unnecessarily).

6️. Output Handling
• Ensure {target_language} output matches {source_language} output exactly (no extra spaces or newlines).
• Do not introduce print statements that do not exist in {source_language}.

7️. Efficient & Idiomatic {target_language} Code (Without Changing Logic)
• Use {target_language} conventions only if needed, but do not rewrite the algorithm in a different way.
• Maintain all sorting, comparisons, and assignments exactly as in {source_language}.

8️. Memory Management & Edge Cases
• If {source_language} function stops reading input after a certain condition, {target_language} must follow the same behavior.
• Handle negative values, boundary conditions, and invalid input exactly as in {source_language}.
• Avoid premature termination unless required.

Here is the {source_language} code that needs to be translated into {target_language}:

{source_code}

Respond with Python output code only. Do not include explanations, comments, or formatting. The output should be a fully executable {target_language} program.
"""

try:
    # Generate a response from Ollama
    response = client.generate(model=model, prompt=prompt)
    translated_code = response["response"]
  
    print("Translated Code in Python:")
    print(translated_code)
except Exception as e:
    print("An error occurred:", e)
