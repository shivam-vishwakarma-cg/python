text=input("enter a string")
index=0
count=0
length=len(text)
while index<length:
    print(text[index],end=" ")
    index+=1
    count+=1
print("count: ",count)