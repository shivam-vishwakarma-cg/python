total=0

luxury=0
premium=0
regular=0
budget=0
pro=int(input("enter no of products to enter"))
for i in range(pro):
    x=int(input("enter product amout: "))
    total=x+total
    if x>5000:
        print("Luxury")
        luxury=luxury+1
    elif x>=2000 and x<=4999:
        print("Premium")
        premium=premium+1
    elif x>=500 and x<=1999:
        print("Regular")
        regular=regular+1
    else:
        print("Budget")
        budget=budget+1
avg=total/pro
print("total of products: ",total)
print("average of products: ",avg)
print("budget: ",budget)
print("premium: ",premium)
print("regular: ",regular)
print("luxury: ",luxury)

