import ollama

# Optimized Few-Shot Examples for C to Python Translation
def few_shot_examples():
    return """
    ### Example 1: Character Input Handling
    C:
    ```c
    #include <stdio.h>
    int main() {
        char c;
        while (scanf("%c", &c) != EOF) {
            printf("%c", c);
        }
        return 0;
    }
    ```
    
    Python:
    ```python
    import sys
    for c in sys.stdin.read():
        print(c, end='')
    ```

    ### Example 2: Mathematical Computation
    C:
    ```c
    #include <stdio.h>
    int factorial(int n) {
        if (n == 0) return 1;
        return n * factorial(n - 1);
    }
    int main() {
        int n;
        scanf("%d", &n);
        printf("%d", factorial(n));
        return 0;
    }
    ```
    
    Python:
    ```python
    import sys
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    n = int(sys.stdin.readline().strip())
    print(factorial(n))
    ```

    ### Example 3: Space-Separated Input & Output Formatting
    C:
    ```c
    #include <stdio.h>
    int main() {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\\n", a + b);
        return 0;
    }
    ```
    
    Python:
    ```python
    import sys
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    ```
    """

# Optimized Chain-of-Thought Prompting
def chain_of_thought_prompt(code):
    return f"""
    ### Chain-of-Thought Breakdown:
    1. **Identify input method**:
       - `scanf("%c", &c) != EOF` reads **one character at a time**.
       - This should be replicated in Python using `sys.stdin.read()`.

    2. **Identify transformations**:
       - `toupper(c)` in C is part of `<ctype.h>`.
       - In Python, we use `str.upper()` instead.

    3. **Identify output method**:
       - `printf("%c", c)` should **preserve exact formatting** with `end=''`.

    ---
    
    ### Now, Translate the Following C Code:

    C:
    ```c
    {code}
    ```

    ---
    
    **Instructions**
    - **Translate this C code to Python** while following the above conventions**.  
    - **Output only the final Python code**.  
    - **Do not include explanations, comments, or extra formatting**.  
    - **Ensure the final Python program is executable as-is**.  
    """

# Generate translation using Ollama's local LLM
def generate_translation(code, model="codellama"):
    """
    Translates a single C code snippet into Python using Ollama.
    """
    # Combine Few-Shot Prompt + Chain-of-Thought
    few_shot_prompt = few_shot_examples()
    cot_prompt = chain_of_thought_prompt(code)
    full_prompt = f"{few_shot_prompt}\n\n{cot_prompt}"

    # Call Ollama for translation
    response = ollama.chat(
        model=model,
        messages=[{"role": "system", "content": "You are an expert in C programming and software development."},
                  {"role": "user", "content": full_prompt}],
        options={"seed": "random", "temperature": 0.2}
    )

    return response["message"]["content"]

# Example C code snippet
c_code = """
#include<stdio.h>
#include<math.h>

int main(){
	int d,r;
	double x,y;
	double rad=90;
	int a,b;
	
	while(scanf("%d,%d",&d,&r)!=EOF){
		if(!d && !r)break;
		
		x+=d*cos(rad*M_PI/180);
		y+=d*sin(rad*M_PI/180);
		
		rad-=r;
	}
	
	a=(int)x;
	b=(int)y;
	
	printf("%d %d\n",a,b);
	
	return 0;
	
}
"""

# Translate code
translated_code = generate_translation(c_code, model="codellama")

# Print translation
print("\n🔹 Translated Python Code:\n", translated_code, "\n")