def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
if __name__ == "__main__":
    print("=== CALCULATOR V2 ===")
    print(f"Sum (a + b): {add(2, 3)}")
    print(subtract(5, 2))

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
