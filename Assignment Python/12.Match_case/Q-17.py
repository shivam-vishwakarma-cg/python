account=int(input("Enter user Type : "))
show=int(input("Enter option : "))
match account:
    case 1:
        match show:
            case 1:
                print("saving check balance")
            case 2:
                print("saving deposite")
            case 3:    
                print("saving withdraw")
    case 2:
        match show:
            case 1:
                print("current check balance")
            case 2:
                print("current deposite")
            case 3:    
                print("current withdraw")
    case _:
        print("invalid")
        