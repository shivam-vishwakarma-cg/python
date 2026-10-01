n=int(input("enter no of students"))
vowel=0
char=0
con=0
for i in range(1,n+1):
    name=input("enter student name")
    length=len(name)
    if name in "aeiouAEIOU":
        vowel=vowel+1
    else:
        con=con+1
    marks=int(input("enter marks"))
    if marks>=90 and marks<=100:
        print("A+")
    elif marks>=80 and marks<=89:
        print("A")
    elif marks>=70 and marks<=79:
        print("B")
    elif marks>=60 and marks<=69:
        print("C")
    elif marks>=50 and marks<=59:
        print("D")
    else:
        print("fail")
    if con>vowel:
        print("consonant win")
    elif vowel>con:
        print("vowel win")
    else:
        print("draw")
    print("total count characters",length)
    print("total vowels",vowel)
print("highest mars of the student")