
sub1=int(input("english"))
if sub1 >=0 and sub1 <=100:
    sub2=int(input("maths"))
if sub1 >=0 and sub1 <=100:  
    sub3=int(input("science"))
if sub1 >=0 and sub1 <=100:

    if sub1>=35:
        avg=(sub1+sub2+sub3)/3
        print("avg",avg)
    else:
        print("fail")
