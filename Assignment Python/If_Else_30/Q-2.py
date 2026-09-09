num=int(input("enter any number"))
if num%2 == 0 and num > 0:
    print("Positive Even")
elif num%2 != 0 and num > 0:
    print("Positive odd")
elif num%2 == 0 and num < 0:
    print("Negative Even")
elif num%2 != 0 and num < 0:
    print("Negative Odd")
elif num == 0:
    print("zero")
else:
    print("wrong value entered")
    