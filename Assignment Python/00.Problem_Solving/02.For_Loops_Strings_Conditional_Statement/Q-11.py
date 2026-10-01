user=int(input("enter no of usernames"))
dig=0
un=0
for i in range(user):
    name=input("enter username")
    if name[0] in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
         print("first character checked")
    for i in name:
        length=len(name)
        if length<=6:
            print("atleast 6 characters")
        elif i in "1234567890":
            dig=dig+1
        elif i in "!@#$%^&*()":
            print("invalid")
        elif i in "_":
            un=un+1
        else:
            print(end="")
print("digits count: ",dig)
print("length: ",length)
print("underscores count: ",un)

