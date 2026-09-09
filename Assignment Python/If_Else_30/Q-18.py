temp=int(input("enter your temperature"))
if temp <0 :
    print("freezing")
elif temp>=0 and temp<=15:
    print("very cold")
elif temp>=16 and temp<=25:
    print("cold")
elif temp>=26 and temp<=35:
    print("normal")
elif temp >55:
    print("hot")
else:
    print("your issue")