def gcd(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean Algorithm.

    :param a: First number (integer).
    :param b: Second number (integer).
    :return: GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Ensure the GCD is always non-negative

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
