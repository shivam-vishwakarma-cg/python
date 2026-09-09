a=int(input("first side"))
b=int(input("second side"))
c=int(input("third side"))
if a+b>c: 
    if a+c>b:
        if b+c>a:
            print("valid triangle")
else:
    print("invalid triangle")