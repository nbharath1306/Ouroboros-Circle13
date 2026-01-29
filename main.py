"""
main.py - The Organism
A Fibonacci calculator with an intentional bug fixed for demonstration.
"""


def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    # Check for negative inputs
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base cases
    if n <= 1:
        return n
    
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    
    # Calculate the nth Fibonacci number
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


if __name__ == "__main__":
    # Test with a value
    test_value = 15
    try:
        print(f"Calculating Fibonacci({test_value})...")
        result = fibonacci(test_value)
        print(f"Result: {result}")
        print("Calculation successful")
    except ValueError as e:
        print(f"Error: {e}")