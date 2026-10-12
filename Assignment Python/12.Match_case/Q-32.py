choice = int(input("1 → Student\n2 → Teacher\n3 → Parent\nEnter role: "))

match choice:
    case 1:
        print("Student")
        choice1 = int(input("1 → Marks\n2 → Attendance\n3 → Homework\nEnter option: "))

        match choice1:
            case 1:
                print("View Student Marks")
            case 2:
                print("View Student Attendance")
            case 3:
                print("View Homework")
            case _:
                print("Invalid option")

    case 2:
        print("Teacher")
        choice2 = int(input("1 → Enter Marks\n2 → Attendance\n3 → Assign Homework\nEnter option: "))

        match choice2:
            case 1:
                print("Enter Student Marks")
            case 2:
                print("Manage Attendance")
            case 3:
                print("Assign Homework")
            case _:
                print("Invalid option")

    case 3:
        print("Parent")
        choice3 = int(input("1 → Child Marks\n2 → Child Attendance\n3 → Contact Teacher\nEnter option: "))

        match choice3:
            case 1:
                print("View Child Marks")
            case 2:
                print("View Child Attendance")
            case 3:
                print("Contact Teacher")
            case _:
                print("Invalid option")

    case _:
        print("Invalid role")   
