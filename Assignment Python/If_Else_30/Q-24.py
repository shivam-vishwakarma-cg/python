amount=int(input("enter purchase amount"))
if amount<500:
    print("amount")
elif amount >=500 and amount<=999:
    a=amount*5/100
    b=amount-a
    print("discounted amount",b)
elif amount >=1000 and amount<=1999:
    c=amount*10/100
    d=amount-c
    print("discounted amount",d)
elif amount>=2000 and amount<=4999:
    e=amount*15/100
    f=amount-e
    print("discounted amount",f)
elif amount>=5000:
    g=amount*20/100
    h=amount-g
else:
    print("error")
    