priority=int(input("Enter priority number : "))
match priority:
    case 1|2:
        print("Normal priority")
    case 3|4:
        print("urgent priority")
    case _:
        print("invalid")