# write a python program to print squares of 1 to n
# Read input from user
n = int(input("Enter the value of n: "))

# Print squares from 1 to n
print(f"Squares of numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(f"{i}^2 = {i ** 2}")
