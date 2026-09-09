cp=int(input("enter cost price"))
sp=int(input("enter selling price"))
p=sp-cp
l=cp-sp
if sp>cp:
    print("profit",p)
elif cp>sp:
    print("loss",l)
elif cp==sp:
    print("no profit no loss")
else:
    print("something wrong")