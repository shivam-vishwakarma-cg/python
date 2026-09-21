a=int(input("first side"))
b=int(input("second side"))
c=int(input("third side"))
if a+b>c: 
    if a+c>b:
        if b+c>a:
            print("valid triangle")
            if a==b==c:
                print("equilateral triangle")
            elif a==b or b==c or c==a:
                print("isosceles triangle")
            else:
                print("scalene triangle")
else:
    print("invalid triangle")