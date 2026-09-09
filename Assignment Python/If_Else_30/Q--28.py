per1=input("enter 1st person name")
age1=int(input("enter 1st person's age"))
per2=input("enter 2st person name")
age2=int(input("enter 2st person's age"))
per3=input("enter 3st person name")
age3=int(input("enter 3st person's age"))
if age1 == age2 == age3:
    print("All three have the same age")

if age1 == age2 or age1 == age3 or age2 == age3:
    print("Two people have the same age")

if age1 < age2 and age1 < age3:
    print(per1, "is the youngest person:", age1)

elif age2 < age1 and age2 < age3:
    print(per2, "is the youngest person:", age2)

else:
    print(per3, "is the youngest person:", age3)