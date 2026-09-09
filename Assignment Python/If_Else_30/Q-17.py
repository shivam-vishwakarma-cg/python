oper=int(input("enter your operation :1.addition 2.substraction 3.multpilication 4.division"))
if oper==1 or oper==2 or oper==3 or oper==4:
    a=int(input("enter your first no"))
    b=int(input("enter your second no"))
    if oper==1:
        c=a+b
        print("your addition value",c)
    elif oper==2:
        c=a-b
        print("your substriction value",c)
    elif oper==3:
        c=a*b
        print("your multiplication value",c)
    elif oper==4:
        c=a/b
        print("your division value",c)
else:
    print("wrong value entered")  
