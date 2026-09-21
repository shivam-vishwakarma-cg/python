num=int(input("enter any number"))
if num>0:
    for i in range(1,num+1):
        if i%2==0 and i%3==0:
            print(i)