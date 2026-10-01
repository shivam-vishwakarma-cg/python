n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        
        if j%2==0:
            print("E ", end="")
        elif j%5==0:
            print("F ",end="")
        else:
            print("O", end="")
            print(end=" ")
    print()