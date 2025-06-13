#write a python prg to read password as input from the user & check whether it is a valid password or invalid password# Read password from the user
pwd = input("Enter password: ")
u=l=s=n=0
for ch in pwd:
    if ch.isupper(): u+=1
    elif ch.islower(): l+=1
    elif ch.isdigit(): n+=1
    else: s+=1
if u and l and s and n: print("Valid password")
else: print("Invalid password")

#write a python prg to read name contact no mail id & password make sure that contact no has only 10 digits mail should have valid structure name @ orgname.com & password should have atleast 3 uppercase alphabets 3 lowercases alphabets 3 spl characters & 1 number& password length should not be less tha 10
name = input("Name: ")
contact = input("Contact (10 digits): ")
email = input("Email: ")
pwd = input("Password: ")

if len(contact)==10 and contact.isdigit() and '@' in email and email.endswith(".com"):
    u=l=s=n=0
    for ch in pwd:
        if ch.isupper(): u+=1
        elif ch.islower(): l+=1
        elif ch.isdigit(): n+=1
        else: s+=1
    if len(pwd)>=10 and u>=3 and l>=3 and s>=3 and n>=1:
        print("Valid input ")
    else:
        print("Invalid password ")
else:
    print("Invalid contact or email ")

#write a python prg to read a string as input from the user & split the string into 3 equal parts using slicing
s = input("Enter a string: ")
n = len(s)

if n % 3 == 0:
    i = n // 3
    print("Part 1:", s[0:i])
    print("Part 2:", s[i:2*i])
    print("Part 3:", s[2*i:])
else:
    print("Cannot split into 3 equal parts")
