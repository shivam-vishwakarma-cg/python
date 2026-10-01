n=int(input("enter no of products"))
dis=0
discount=0
for i in range(n):
    price=int(input("enter price of product"))
    if price>=5000:
        fp=price*(20/100)
        discount=price-fp
        print("discounted price",discount)
        dis=dis+1
    elif price>=3000:
        fp=price*(15/100)
        discount=price-fp
        print("discounted price",discount)
        dis=dis+1
    elif price>=1000:
        fp=price*(10/100)
        print("discounted price",discount)
        discount=price-fp
        dis=dis+1
    else:
        print("no discount",price)
print("Total producs received each discount: ",dis)
print("Total discount: ",fp)



