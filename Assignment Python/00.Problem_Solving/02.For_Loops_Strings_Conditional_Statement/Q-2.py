stu=int(input("enter no of student"))
for i in range(stu):
    mark=int(input("enter marks"))
    if mark >=75 and mark<=100:
        print("Excellent")
    elif mark>=50 and mark<=74:
        print("Good")
    elif mark>=35 and mark<=49:
        print("Pass")
    else:
        print("Fail")
    