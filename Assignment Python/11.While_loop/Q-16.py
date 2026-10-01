n=int(input("enter a number"))
add=0
while n and n>0:
    print(n,end="+")
    add=add+n
    n-=1
print()
print("add",add)