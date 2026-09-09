num=int(input("enter a number"))
if num%7 == 0 and num%3 == 0:
    print("Divisible by both 3 and 7")
elif num%7 == 0:
    print("divisible by 7")
elif num%3 == 0:
    print("divisible by 3")
else:
    print("nothing is divisible by 3 and 7")