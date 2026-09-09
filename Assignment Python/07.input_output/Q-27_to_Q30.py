#27
first_number,sencond_number=map(int,input("Enter 2 no. : ").split())
print(f"No. 1 : {first_number} and No.2 : {sencond_number} \n Sum : {first_number+sencond_number}")
#28
price=float(input("Enter price : "))
quantity=int(input("Enter quantity : "))
Total=price*quantity
print(f"price : {price} , quantity : {quantity} , Total : {Total}")
#29
s_name=input("Enter student name : ")
s_age=int(input("Enter student age : "))
s_marks=float(input("Enter student marks : "))
print(f"name : {s_name} age : {s_age} marks : {s_marks}")
#30
student_name=input("Enter student name : ")
student_age=int(input("Enter student age : "))
student_height=float(input("enter student height : "))
student_city=input("Enter student city : ")
print(f"name {student_name}\nage : {student_age}\nheight : {student_height}\ncity : {student_city}")

#:.2f means format the number as a floating-point value with exactly 2 decimal places.
print(f"{student_height:.2f}")
