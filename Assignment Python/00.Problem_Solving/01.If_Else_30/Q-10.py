vote=int(input("enter your age"))
if vote >=18:
    print("can vote")
elif vote <18 and vote >=1:
    print("can't vote")
else:
    print(" invalid age")