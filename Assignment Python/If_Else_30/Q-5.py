num=int(input("enter first number"))
nnum=int(input("enter second number"))
nnnum=int(input("enter third number"))
if num>nnum:
    if num>nnnum:
        print("smallest number",num)
elif nnum>nnnum:
    if nnum>num:
        print("smallest number",nnum)
elif nnnum>num:
    if nnnum>nnum:
        print("smallest number",nnnum)
else:
    print("something is wrong")