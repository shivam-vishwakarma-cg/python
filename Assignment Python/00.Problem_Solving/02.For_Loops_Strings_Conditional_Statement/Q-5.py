sen=input("enter sentence")
length=len(sen)
if length>6:
    print("long")
elif length>=4 and length<=6:
    print("Medium")
elif length<=3:
    print("short")
else:
    print("error")