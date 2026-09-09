#D. Nested Conditions

#16
age=int(input("enter age : "))

if age>18:
    if age<60:
        print("age is between 18 and 60")
else:
    print("age is less the 18")


#17
marks=int(input("Enter your marks : "))

if marks>=40:
    if marks>75:
        print("Good\n")
    print("pass")
else:
    print("fail")

#18
number=int(input("Enter num : "))
if number>0:
    if(number>100):
        print("grater then 100")
    print("positive")
elif number<0:
    print("negative")
else:
    print("zero")

#19
years = int(input("Enter your age: "))

if years >= 18:
    if years >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")

#20
value = int(input("Enter a number: "))

if value != 0:
    if value > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")
