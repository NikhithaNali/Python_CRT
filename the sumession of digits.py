# write a python program to read the integer value as input from the user & find the sumession of digits
# Read input from user
num = int(input("Enter an integer: "))
Temp = num
# Initialize sum
digit_sum = 0

# Calculate sum of digits
while num != 0:
    digit = num % 10
    digit_sum += digit
    num = num // 10

# Print result
print(f"Sum of digits of {Temp} is {digit_sum}")
