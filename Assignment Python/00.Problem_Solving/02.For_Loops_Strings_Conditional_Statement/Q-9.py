string=str(input("enter a string"))
count=0
v=0
c=0
d=0
s=0
for i in string:
    count=count+1
    print("character",i)
    print("position: ",count)
    if count%2==0:
        print("positon is even")
    else:
        print("position is odd")
    if i in "aeiou":
        print("character is vowel")
        v=v+1
    elif i in "qwrtypsdfghjklzxcvbnm":
        print("character is consonant")
        c=c+1
    elif i in "1234567890":
        print("character is digit")
        d=d+1
    else:
        print("character is special character")
        s=s+1
print("total no of characters",count)
print("total no of vowel",v)
print("total no of consonant",c)
print("total no of digit",d)
print("total no of special character",s)
