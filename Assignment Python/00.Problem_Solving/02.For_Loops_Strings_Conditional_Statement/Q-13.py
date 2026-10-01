cu=int(input("enter no of customers"))
for i in range(cu):
    bill=int(input("enter electricity bill"))
    if bill<=100:
        x=bill*5
        print("bill",x)
    elif bill>=100 and bill<=200:
        x=(100*5)+(bill-100)*7
        print("bill",x)
    elif bill>=200 and bill<=400:
        x=(100*5)+(100*7)+(bill-200)*10
        print("bill",x)
    elif bill>400:
        x=(100*5)+(100*7)+(200*10)+(bill-400)*15
        print("bill",x)
    else:
        print("negative bill???")
    if x>3000:
        print("high")
    elif x>=1000 and bill<=3000:
        print("medium")
    else:
        print("low")
    