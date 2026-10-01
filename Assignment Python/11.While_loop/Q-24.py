text=input("enter a string")
index=0
count=0
a=0
length=len(text)
while index<length:
    print(text[index],end=" ")
    if text[index]=="a":
        a+=1
    index+=1
    count+=1
print("count: ",count)
print("a=",a)