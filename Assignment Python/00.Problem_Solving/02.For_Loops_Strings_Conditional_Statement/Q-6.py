for i in range(5):
    even=0
    odd=0
    x=int(input("enter any number"))
    string=str(x)
    print("now number is in string",string,type(string))
    for i in range(1,x+1):
        print(i)
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print("number of even: ",even)
    print("number of odd: ",odd)
    if even==odd:
        print("both are equal")
    elif even>odd:
        print("even is more than odd")
    else:
        print("odd is more than even")
    