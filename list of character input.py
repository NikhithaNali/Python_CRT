#write a python prg to read the list of character input from the user covert into a word and print it
size=int(input("enter the length of list :"))
char_list=[]
for i in range(size):
    ch=input("enter the character :")
    char_list.append(ch)
print(char_list)
str="".join(char_list)
print(str)
