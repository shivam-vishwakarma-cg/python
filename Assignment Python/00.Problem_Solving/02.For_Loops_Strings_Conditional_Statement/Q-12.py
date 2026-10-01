sen=input("enter a sentence")
con=0
vo=0
for i in sen:
    if i in "aeiouAEIOU":
        vo=vo+1
    else:
        con=con+1
print("no of vowel",vo)
print("no of consonant",con)
if con==vo:
    print("Draw")
elif con>vo:
    print("Consonant Wins")
else:
    print("vowel win")
    