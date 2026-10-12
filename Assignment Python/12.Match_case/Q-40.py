choice = int(input("1 → Student\n2 → Teacher\n3 → Administration\nEnter role: "))

match choice:
    case 1:
        print("Student")
        choice1 = int(input("1 → Profile\n2 → Marks\n3 → Attendance\n4 → Courses\nEnter option: "))

        match choice1:
            case 1:
                print("View Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("View Student Attendance")
            case 4:
                print("View Student Courses")
    case 2:
        print("Teacher")
        choice2 = int(input("1 → Students\n2 → Enter Marks\n3 → Attendance\n4 → Courses\nEnter option: "))

        match choice2:
            case 1:
                print("View Students")
            case 2:
                print("Enter Student Marks")
            case 3:
                print("Manage Attendance")
            case 4:
                print("View Teacher Courses")
    case 3:
        print("Administration")
        choice3 = int(input("1 → Fees\n2 → Admissions\n3 → Notices\n4 → Departments\nEnter option: "))

        match choice3:
            case 1:
                print("Manage Fees")
            case 2:
                print("Manage Admissions")
            case 3:
                print("View Notices")
            case 4:
                print("View Departments")