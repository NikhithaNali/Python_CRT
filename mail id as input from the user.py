# write a python prg to read mail id as input from the user and print user name and organization name based on mail id(name@orgname.com)
email = input("Enter email: ")
name = email.split('@')[0]
org = email.split('@')[1].split('.')[0]
print("User name:", name)
print("Organization name:", org)

