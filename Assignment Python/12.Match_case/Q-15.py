membership = int(input("Enter membership level: "))

match membership:
    case 1 | 2:
        print("Basic Membership")

    case 3 | 4:
        print("Premium Membership")

    case _:
        print("Invalid Membership")