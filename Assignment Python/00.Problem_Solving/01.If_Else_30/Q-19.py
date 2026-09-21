num=int(input("enter a number"))
if num<0:
    print("negative")
elif num >=0 and num<=10:
    print("0-10")
elif num>=11 and num<=50:
    print("11-50")
elif num>=51 and num<=100:
    print("51-100")
elif num>100:
    print("above 100")
else:
    print("your issue")