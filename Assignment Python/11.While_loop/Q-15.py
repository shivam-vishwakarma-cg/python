i=int(input("enter a number"))
count=0
while i>0 and i<50:
    if i%2==0:
        print(i)
        count+=1
        print("count: ",count)
    i+=1