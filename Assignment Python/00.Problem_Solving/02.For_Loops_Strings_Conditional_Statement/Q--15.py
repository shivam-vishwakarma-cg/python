
n=int(input("Enter n"))
even=0
odd=0
pos=0
neg=0
zero=0

for i in range(1,n+1):
    for j in range(1,n+1):
        num=int(input("number: "))
        if num==0:
            print("zero")
            zero=zero+1
        if num%2==0:
            print("even")
            even=even+1
        if num%3==0:
            print("odd")
            odd=odd+1
        if num>0:
            print("positive")
            pos=pos+1
        if num<0:
            print("negative")
            neg=neg+1
        else:
            print(end="")
    print()
    
    
print("even count: ",even)
print("odd count: ",odd)
print("positive count: ",pos)
print("negative count: ",neg)
print("zero count: ",zero)
print("largest no: ")
