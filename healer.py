"""
healer.py - The AI Doctor
Uses Groq to analyze errors and fix the code automatically.
"""
import os
from groq import Groq


def read_file(filepath):
    """Read file contents"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def heal_code():
    """Use Groq AI to fix the broken code"""
    # Initialize Groq client
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found in environment variables")
        return False
    
    client = Groq(api_key=api_key)
    
    # Read the broken code and error log
    current_code = read_file("main.py")
    error_log = read_file("error.log")
    
    if not current_code:
        print("❌ main.py not found")
        return False
    
    if not error_log:
        print("⚠️  No error.log found, but attempting to optimize code anyway")
        error_log = "No specific error. Optimize the code to handle larger inputs."
    
    print("🧬 Analyzing error and generating fix...")
    print(f"📋 Error context: {error_log[:200]}")
    
    # Create prompt for Groq
    prompt = f"""The following Python code has an error:

ERROR LOG:
{error_log}

CURRENT CODE:
{current_code}

Fix the error and return the complete corrected Python code. The code should:
1. Fix any runtime errors or exceptions
2. Handle edge cases properly
3. Maintain the same functionality
4. Be production-ready and robust

Return ONLY the fixed Python code, nothing else. No markdown, no explanations."""
    
    try:
        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python Expert. Fix the error in the code. Return ONLY the full valid Python code. No markdown."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=2000
        )
        
        fixed_code = response.choices[0].message.content.strip()
        
        # Remove markdown code blocks if present
        if fixed_code.startswith("```python"):
            fixed_code = fixed_code.split("```python")[1].split("```")[0].strip()
        elif fixed_code.startswith("```"):
            fixed_code = fixed_code.split("```")[1].split("```")[0].strip()
        
        # Validate the fixed code
        try:
            compile(fixed_code, '<string>', 'exec')
            print("✅ Generated code is syntactically valid")
        except SyntaxError as e:
            print(f"❌ Generated code has syntax errors: {e}")
            return False
        
        # Write fixed code back to main.py
        with open("main.py", 'w') as f:
            f.write(fixed_code)
        
        print("✅ Code healed successfully!")
        print("💾 Updated main.py with fixed code")
        return True
        
    except Exception as e:
        print(f"❌ Healing failed: {str(e)}")
        return False


if __name__ == "__main__":
    print("🏥 AI Doctor activated...")
    print("=" * 60)
    
    success = heal_code()
    
    print("=" * 60)
    if success:
        print("🎉 Healing complete! The organism should now survive.")
        exit(0)
    else:
        print("💀 Healing failed. Manual intervention required.")
        exit(1)
