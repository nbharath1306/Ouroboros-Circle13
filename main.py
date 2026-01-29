"""
main.py - The Organism
A Fibonacci calculator with an intentional bug for demonstration.
"""


def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    # Intentional bug: Raise error for inputs > 10
    if n > 10:
        raise ValueError("Input too large! This organism is weak and will crash.")
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    # Test with a value that triggers the bug
    test_value = 15
    print(f"Calculating Fibonacci({test_value})...")
    result = fibonacci(test_value)
    print(f"Result: {result}")
    print("Calculation successful")
