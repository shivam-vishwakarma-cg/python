cp=int(input("enter cost price"))
sp=int(input("enter selling price"))
p=sp-cp
l=cp-sp
w=p/cp*100
n=l/cp*100
if sp>cp:
    print("profit percent",w,"%")
elif cp>sp:
    print("loss percent",n,"%")
elif cp==sp:
    print("no profit no loss")
else:
    print("something wrong")