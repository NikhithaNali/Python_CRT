# write a python program to print natural numbers from 1 to n
# Read input from user
n = int(input("Enter the value of n: "))

# Print natural numbers from 1 to n
print(f"Natural numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
