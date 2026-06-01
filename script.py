"""
Utility Script - A collection of helpful utility functions
"""

def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers (with zero check)."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0


def reverse_string(text):
    """Reverse a string."""
    return text[::-1]


def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def main():
    """Main function to demonstrate utilities."""
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Reverse of 'Hello' = {reverse_string('Hello')}")
    print(f"Vowels in 'Python' = {count_vowels('Python')}")


if __name__ == "__main__":
    main()
