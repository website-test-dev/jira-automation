# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

# TODO: We need multiplication and division functions here.

if __name__ == "__main__":
    print("Welcome to the Calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 5 = {multiply(4, 5)}")