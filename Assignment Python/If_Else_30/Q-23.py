user=input("enter your username")

Username = "admin"
Password = "python123"


if Username==user:
    password=input("enter your password")

    if Password==password:
        print("login successful")
    elif Password!=password:
            print("wrong password")
elif Username!=user:
    print("User not found")

    
else:
    print("reset your password")