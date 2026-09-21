num=int(input("enter a number"))
if num%11 == 0 and num%5 == 0:
    print("Divisible by both 5 and 11")
elif num%11 == 0:
    print("divisible by 11")
elif num%5 == 0:
    print("divisible by 5")
else:
    print("nothing is divisible by 5 or 11")