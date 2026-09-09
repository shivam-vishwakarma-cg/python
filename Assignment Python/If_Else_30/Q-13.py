char=input("enter any character")
if char in "aeiou":
    print("vowel")
elif char not in "aeiou":
    print("consonant")
else:
    print("invaild input")