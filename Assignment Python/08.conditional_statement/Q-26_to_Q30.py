#26
is_close=False
if not is_close:
    print("open")

#27
x=int(input("Enter num : "))
if x>10 and x<50:
    print("Greater than 10 and less the 50")

#28
y=int(input("Enter num : "))
if not y>10 and y<50:
    print("not --- Greater than 10 and less the 50")

#29
is_student = True
has_id = True
has_ticket = False

if is_student and has_id and has_ticket:
    print("Entry allowed")
else:
    print("Entry not allowed")

#30
marks=int(input("Enter your marks : "))
age=int(input("Enter your age : "))
has_id1=(input("enter True or False : "))

if marks>=40 and age >=18 and has_id1=="True":
    print("eligible")
else:
    print("not eligible")