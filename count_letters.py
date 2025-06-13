# write a python prog to read a string as a input from the user & print no.of
# 1) count of uppercase letters
# 2.count of lowercase letters
# 3.print the count of numeric values
# 4.print the count of special characters
str=input("enter the string :")
uppercase_alpha=0
lowercase_alpha=0
numeric=0
special_char=0
for ch in str:
    if ch.isupper():
        uppercase_alpha+=1
    elif ch.islower():
        lowercase_alpha+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
print("upper count",uppercase_alpha)
print("lower count",lowercase_alpha)
print("numeric count",numeric)
print("special character",special_char)
