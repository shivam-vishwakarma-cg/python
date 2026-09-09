unit=int(input("enter electric units"))
if unit <0:
    print("invalid")
if unit <= 100:
    a=unit*5
    print(a)
elif unit >100 and unit <= 200:
    b=(100*5) + (unit-100)*7
    print(b)
elif unit >200:
    c=(100*5) + (100*7) + ((unit-200)*10)
    print(c)
else:
    print("something is wrong")