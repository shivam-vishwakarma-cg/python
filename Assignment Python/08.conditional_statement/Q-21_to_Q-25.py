#E. Multiple Conditions

#21
age=int(input("enter age : "))
marks=int(input("Enter your marks : "))

if age>=18 and marks>=40:
    print("eligible")


#22
number=int(input("Enter num : "))
if number<10 or number>100:
    print("special")


#23
age1=int(input("enter age : "))
has_id=int(input("Enter 1 for yes and 0 for no"))
if age1>=18 and has_id==1:
    print("allowed")

#24
a,b=map(int,input("enter 2 no. ").split())
if a>10 and b>10:
    print("Both are greater than 10")

#25
number1=int(input("Enter num : "))

if number1<0 or number1>100:
    print("less than 0 or greater than 100")