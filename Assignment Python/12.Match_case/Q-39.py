choice=int(input("1 → Employee\n2 → Manager Enter : "))
match choice:
    case 1:
        print("Employee")
        choice1=int(input("1 → View Profile\n2 → Apply Leave\n3 → View Salary : "))

        match choice1:
            case 1:
                print("view profile")
            case 2:
                print("apply leave")
                leave=int(input("Enter number of leave : "))
                if leave>0:
                    print("Leave Request Submitted")
                else:
                    print("invalid leave request")
            case 3:
                print("view salary")
    case 2:
        print("manager")
        choice2=int(input("1 → View Team\n2 → Approve Leave\n3 → View Reports\nEnter choice: "))
        match choice2:
            case 1:
                print("view team")
            case 2:
                print("approve leave")
            case 3:
                print("view reports")