# write a python program to print natural numbers from n to 1
# Read input from user
n = int(input("Enter the value of n: "))

# Print natural numbers from n to 1
print(f"Natural numbers from {n} to 1:")
for i in range(n, 0, -1):
    print(i, end=" ")