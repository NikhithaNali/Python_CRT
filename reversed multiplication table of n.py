#write a python program to print the reversed multiplication table of n
n = int(input("Enter the value of n: "))
print(f"\nReversed Multiplication Table of {n}:")
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")





