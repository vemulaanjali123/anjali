# Python Program to Print the Fibonacci sequence using while loop

# Number of terms to display
n_terms = int(input("Enter the number of Fibonacci terms to display: "))

# First two terms
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a, end=" ")
        # Update values
        a, b = b, a + b
        count += 1
