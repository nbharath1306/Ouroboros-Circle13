"""
architect.py - The Brain
Uses LLM (Groq) to analyze errors and generate fixed code.
"""
import os
from groq import Groq
from typing import Tuple


class Architect:
    """The Brain - Uses AI to fix code"""
    
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"  # Fast and smart model
        
    def analyze_and_fix(self, error_log: str, current_code: str, mutation_type: str = "ERROR") -> Tuple[str, str]:
        """
        Analyze error and generate fixed code.
        
        Args:
            error_log: The error traceback or performance issue
            current_code: The current organism.py code
            mutation_type: "ERROR" for crashes, "OPTIMIZATION" for performance
            
        Returns:
            Tuple of (fixed_code, explanation)
        """
        
        if mutation_type == "OPTIMIZATION":
            prompt = self._create_optimization_prompt(current_code, error_log)
        else:
            prompt = self._create_fix_prompt(error_log, current_code)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert Python debugger and optimizer. Return ONLY valid Python code without any markdown formatting, explanations, or code blocks. The code must be complete and ready to execute."
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
            
            # Generate explanation
            explanation = self._generate_explanation(error_log, mutation_type)
            
            return fixed_code, explanation
            
        except Exception as e:
            raise Exception(f"Failed to generate fix: {str(e)}")
    
    def _create_fix_prompt(self, error_log: str, current_code: str) -> str:
        """Create prompt for fixing errors"""
        return f"""The following Python code crashed with this error:

ERROR:
{error_log}

CURRENT CODE:
{current_code}

Fix the error and return the complete corrected Python code. The code should:
1. Fix the syntax or runtime error
2. Maintain the same functionality
3. Keep the same structure (imports, functions, if __name__ block)
4. Be production-ready

Return ONLY the fixed Python code, nothing else."""
    
    def _create_optimization_prompt(self, current_code: str, performance_info: str) -> str:
        """Create prompt for optimization"""
        return f"""The following Python code is running too slowly:

PERFORMANCE ISSUE:
{performance_info}

CURRENT CODE:
{current_code}

Optimize the code to run faster. Focus on:
1. Improving time complexity (e.g., replace O(n²) with O(n log n))
2. Using efficient built-in functions
3. Maintaining the same functionality
4. Keeping the code readable

Return ONLY the optimized Python code, nothing else."""
    
    def _generate_explanation(self, context: str, mutation_type: str) -> str:
        """Generate human-readable explanation of the fix"""
        if mutation_type == "OPTIMIZATION":
            return f"Optimized code for better performance: {context[:100]}"
        else:
            # Extract key error info
            if "ZeroDivisionError" in context:
                return "Fixed: Division by zero error"
            elif "SyntaxError" in context:
                return "Fixed: Syntax error in code"
            elif "NameError" in context:
                return "Fixed: Undefined variable reference"
            elif "IndexError" in context:
                return "Fixed: List index out of range"
            elif "TypeError" in context:
                return "Fixed: Type mismatch error"
            else:
                return f"Fixed: {context.split(':')[0] if ':' in context else 'Code error'}"


# Global architect instance
architect = None


def get_architect():
    """Get or create the architect instance"""
    global architect
    if architect is None:
        architect = Architect()
    return architect
