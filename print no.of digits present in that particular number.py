# write a python program to read an integer value as a user and print no.of digits present in that particular number
# Read input from user
num = int(input("Enter an integer: "))
Temp=num
Digitcount=0
while(num>=0):
    num=num//10
    Digitcount+=1
print(f"{Temp} has {Digitcount} digits")


