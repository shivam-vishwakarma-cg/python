num=int(input("enter first number"))
nnum=int(input("enter 2nd number"))
if num>nnum:
    print("largest no",num)
elif nnum>num:
    print("largest no",nnum)
elif num==nnum:
    print("both are equal")
else:
    print("entered wrong value")