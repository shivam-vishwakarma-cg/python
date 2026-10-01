sen=input("enter a sentence")
point=0
con=0
vowel=0
dig=0
sc=0
for i in sen:
    if i in "qwrttypsdfghjklzxcvbnm":
        con=con+1
        point=point+1
    elif i in "aeiou":
        vowel=vowel+1
        point=point+2
    elif i in "1234567890":
        dig=dig+1
        point=point+3
    else:
        sc=sc+1
        point=point+4
print("consonant",con)
print("vowel",vowel)
print("digit",dig)
print("special character",sc)
print("points",point)
