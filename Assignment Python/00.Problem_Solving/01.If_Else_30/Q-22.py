amount=int(input("enter your amount balance"))
draw=int(input("enter your withdrawal amount"))
if amount>0:
    if amount%100 == 0:
        if amount>draw:
            if amount>= 500:
                print("rules checked")
                a=amount-draw
                print("your remaining amount",a)
                print("withdrawal amount",draw)
            else:
                print("something is wrong with your wallet")
