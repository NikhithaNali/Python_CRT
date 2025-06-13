str=input("enter the string :")
u_vowels=l_vowels=u_consonants=l_consonants=0
for ch in str:
    # if(ch.isalpha()and ch.isupper()):
    if(ch>='A' and ch<='Z'):
        if ch in "AEIOU":
            u_vowels+=1
        else:
            u_consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in "aeiou":
            l_vowels+=1
        else:
            l_consonants+=1
print(f"lower case vowels count: {l_vowels}")
print(f"lower case consonants count: {l_consonants}")
print(f"upper case vowels count: {u_vowels}")
print(f"upper case consonants count: {u_consonants}")