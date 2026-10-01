u=0
l=0
d=0
s=0

pas=input("enter password")
length=len(pas)
for i in pas:
    if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
        u=u+1
    elif i in "qwertyuiopasdfghjklzxcvbnm":
        l=l+1
    elif i in "1234567890":
        d=d+1
    elif i in "!@#$%^&*()":
        s=s+1
    else:
        print("error")
    x=int(u)
    y=int(l)
    z=int(d)
    g=int(s)

print("percentage of uppercase in password",x/length*100)
print("percentage of lowercase in password",y/length*100)
print("percentage of digit in password",z/length*100)
print("percentage of special character in password",g/length*100)


