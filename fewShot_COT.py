import ollama

# Optimized Few-Shot Examples for C to Python Translation
def few_shot_examples():
    return """
    ### Example 1: Basic Arithmetic (Batch Processing)
    C:
    ```c
    #include <stdio.h>

    int main() {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d", a + b);
        return 0;
    }
    ```
    
    Python:
    ```python
    def add_numbers(batch_inputs):
        results = []
        for line in batch_inputs:
            a, b = map(int, line.split())
            results.append(a + b)
        return results
    ```

    ### Example 2: Factorial Calculation
    C:
    ```c
    #include <stdio.h>

    int factorial(int n) {
        if (n == 0) return 1;
        return n * factorial(n - 1);
    }

    int main() {
        int num;
        scanf("%d", &num);
        printf("%d", factorial(num));
        return 0;
    }
    ```
    
    Python:
    ```python
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)

    def process_factorial(batch_inputs):
        return [factorial(int(n)) for n in batch_inputs]
    ```

    ### Example 3: Handling Arrays
    C:
    ```c
    #include <stdio.h>

    int main() {
        int n, i;
        scanf("%d", &n);
        int arr[n];
        for (i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
        }
        for (i = n-1; i >= 0; i--) {
            printf("%d ", arr[i]);
        }
        return 0;
    }
    ```
    
    Python:
    ```python
    def reverse_array(batch_inputs):
        results = []
        for line in batch_inputs:
            numbers = list(map(int, line.split()))
            results.append(" ".join(map(str, numbers[::-1])))
        return results
    ```
    """

# Optimized Chain-of-Thought Prompting for batch processing as well as single input cases

def chain_of_thought_prompt(code):
    return """
    ### Chain-of-Thought Breakdown:
    
    1. **Detect Input Handling Needs**:
       - If the C program **reads input inside a `while(scanf(...))` loop**, use **`sys.stdin` for batch input**.
       - If the C program **reads only once**, use **`sys.stdin.readline()` instead of `input()`**.
       - If `gets()` or `fgets()` is used, use **`sys.stdin.read()` to read multi-line input**.

    2. **Detect Loop Behavior**:
       - If `while(scanf(...)) != EOF` or `for (...) { scanf(...) }` exists, convert it into **`for line in sys.stdin:`**.
       - If input is **only read once**, keep `sys.stdin.readline().strip()` instead of batch input.

    3. **Output Formatting**:
       - Always ensure correct **output formatting** using `print(f"...")` or `" ".join(map(str, ...))`.

    ---
    
    ### Example 1: Batch Processing Needed
    #### **C Code:**
    ```c
    #include <stdio.h>

    int main() {
        int a, b;
        while (scanf("%d %d", &a, &b) != EOF) {
            printf("%d\\n", a + b);
        }
        return 0;
    }
    ```
    #### **Python Translation (Batch Processing Applied):**
    ```python
    import sys
    for line in sys.stdin:
        a, b = map(int, line.strip().split())
        print(a + b)
    ```

    ---
    
    ### Example 2: Single Input Case (No Batch Processing)
    #### **C Code:**
    ```c
    #include <stdio.h>

    int main() {
        int num;
        scanf("%d", &num);
        printf("%d\\n", num * 2);
        return 0;
    }
    ```
    #### **Python Translation (Single Input Only):**
    ```python
    import sys
    num = int(sys.stdin.readline().strip())
    print(num * 2)
    ```

    ---
    
    ### Now, Translate the Following C Code:

    C:
    ```c
    """ + code +"""
    ```

    ---
    
    **Instructions**
    - **Translate this C code to Python** following best practices.
    - **If `while(scanf(...)) != EOF` is used, always use `sys.stdin` for batch input**.
    - **If `scanf()` appears only once, use `sys.stdin.readline().strip()` instead**.    
    - **Return only valid Python code, without explanations or comments**.  
    - **Make sure the output is an executable Python script**.  
    """


# Optimized Chain-of-Thought Prompting for batch processing only

# def chain_of_thought_prompt(code):
#     return """
#     ### Chain-of-Thought Breakdown:
#     1. **Input Handling**:
#        - C uses `scanf()` for reading input, often in a loop.
#        - **Do not use `input()` in Python**; instead, use `sys.stdin.read()` for batch processing.
#        - If multiple values are expected per line, split them using `.split()` or `.strip().split()`.

#     2. **Loop Conversion**:
#        - If the C program processes input in a `while(scanf(...) != EOF)` loop, **use a for loop over `sys.stdin`**.
#        - Example: `for line in sys.stdin:` instead of manual `input()` calls.

#     3. **Output Formatting**:
#        - Use `print()` but ensure formatted output using `f-strings` or `.join(map(str, ...))`.

#     ---
    
#     ### Example 1: Simple Input Processing
#     #### **C Code:**
#     ```c
#     #include <stdio.h>

#     int main() {
#         int a, b;
#         while (scanf("%d %d", &a, &b) != EOF) {
#             printf("%d\\n", a + b);
#         }
#         return 0;
#     }
#     ```
#     #### **Python Translation (Corrected for Batch Input):**
#     ```python
#     import sys
#     for line in sys.stdin:
#         a, b = map(int, line.strip().split())
#         print(a + b)
#     ```

#     ---
    
#     ### Now, Translate the Following C Code:

#     C:
#     ```c
#     """ + code + """
#     ```

#     ---
    
#     **Instructions**
#     - **Always use `sys.stdin` for batch input handling instead of `input()`**.
#     - **Ensure that input is processed in loops using `for line in sys.stdin`**.
#     - **Return only valid Python code, without explanations or extra formatting**.
#     """



# Generate translation using Ollama's local LLM
def generate_translation(code, model="codellama"):
    # Translates a single C code snippet into Python using Ollama.

    # Combine Few-Shot Prompt + Chain-of-Thought
    few_shot_prompt = few_shot_examples()
    cot_prompt = chain_of_thought_prompt(code)
    full_prompt = f"{few_shot_prompt}\n\n{cot_prompt}"

    # Call Ollama for translation
    response = ollama.chat(
        model=model,
        messages=[{"role": "system", "content": "You are a skilled software developer proficient in multiple programming languages. Your task is to accurately rewrite the following C code into Python while preserving all functionality and logic exactly."},
                  {"role": "user", "content": full_prompt}],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]

# Example C code snippet
c_code = """
#include <stdio.h>
int main(){
   int n;
   int a,b,c;
   
   a=b=c=0;
   
   for(int i=0;i<10;i++){
       scanf("%d",&n);
       if(n>=a){
           c=b;b=a;a=n;
       }else if(n>=b){
           c=b,b=n;
       }else if(n>c){
           c=n;
       }
   }
   printf("%d\n%d\n%d\n",a,b,c);
   
   return(0);
   
}
"""

# Translate code
translated_code = generate_translation(c_code, model="codellama")

# Print translation
print("\n🔹 Translated Python Code:\n", translated_code, "\n")