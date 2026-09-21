mask=int(input("enter your marks"))
if mask >= 90 and mask <=100:
    print("A")
elif mask >=80 and mask <=89:
    print("B")
elif mask >=70 and mask <=79:
    print("C")
elif mask >=60 and mask <=69:
    print("D")
elif mask >=40 and mask <=59:
    print("E")
elif mask >=0 and mask <=40:
    print("Fail")
else:
    print("something is wrong")