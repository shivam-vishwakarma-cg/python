choice=int(input("Enter 1 → Personal Banking \n2 → Business Banking : "))
match choice:
    case 1:
        print("Personal Banking")
        choice1=int(input("1 → Balance 2 → Transfer 3 → Loan : "))
        match choice1:
            case 1:
                print("balance")
            case 2:
                print("transfer")
            case 3:
                print("loan")
            case _:
                print("invalid choice")
    case 2:
        print("bussiness banking")
        choice2=int(input("Enter 1 → Balance 2 → Payroll 3 → Business Loan"))
        match choice2:
            case 1:
                print("balance")
            case 2:
                print("payroll")
            case 3:
                print("business loan")
            case _:
                print("invalid choice")
    case _:
        print("invalid choice")