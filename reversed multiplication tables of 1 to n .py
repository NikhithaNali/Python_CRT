#write a python program to print the reversed multiplication tables of 1 to n 
n = int(input("Enter the value of n: "))
# Print reversed multiplication tables from 1 to n
for num in range(1, n + 1):
    print(f"\nReversed Multiplication Table of {num}:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")