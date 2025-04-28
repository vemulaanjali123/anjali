# Input interval from user
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num < 2:
        continue  # Skip numbers less than 2 (not prime)
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Not a prime number
    if is_prime:
        print(num, end=" ")
