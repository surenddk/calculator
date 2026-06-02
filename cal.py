def addition(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def subtraction(a, b):
    """
    Subtract two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The difference of a and b
    """
    return a - b


# Example usage
if __name__ == "__main__":
    result = addition(5, 3)
    print(f"5 + 3 = {result}")
    
    result = subtraction(5, 3)
    print(f"5 - 3 = {result}")
