x=input("enter any string containing letters, digits, spaces and special characters")
count =0
count1=0
count2=0
count3=0
for i in x:
    if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
        count =count+1
        print(count)
    elif i in "qwertyuiopasdfghjklzxcvbnm":
        count1=count1+1
        print(count1)
    elif i in "1234567890":
        count2=count2+1
        print(count2)
    else:
        count3=count3+1
        print(count3)
print()

