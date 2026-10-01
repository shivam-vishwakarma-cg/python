trans=int(input("enter no of transactions"))
acc=0
tran=0
for i in range(trans):
    tr=input("Deposit or Withdrawal: ")
   
    if tr== "deposit":
        amount=int(input("enter amount to be deposit"))
        acc=amount+acc
        print("Updated balance",acc)
    elif tr== "withdrawal":
        amount=int(input("enter amount to be withdrawal"))
        if amount<acc and acc>1000:
            acc=acc-amount
            print("balance",acc)
            print("amount withdraw")
            print("Updated balance",acc)
            tran=tran+1
        else:
            print("Low Balance")
print("final balance",acc)
print("Transaction count",tran)
