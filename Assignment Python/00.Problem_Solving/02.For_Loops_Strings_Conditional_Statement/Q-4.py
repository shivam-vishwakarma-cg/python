user=int(input("enter no of users: "))
for i in range(user):
    pas=input("enter your password: ")
    length=len(pas)
    print("length of password: ",length)
    if length>=8:
        print("minimum length satisfied")
        if pas in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            print("Weak")
        elif pas in "1234567890":
            print("Medium")
        else:
            print("Strong")
