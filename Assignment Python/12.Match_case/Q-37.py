choice = int(input("1 → Programming\n2 → Mathematics\n3 → Communication\nEnter subject: "))

match choice:
    case 1:
        print("Programming")
        choice1 = int(input("1 → Python\n2 → Java\n3 → C++\nEnter course: "))

        match choice1:
            case 1:
                print("Python Course Selected")
            case 2:
                print("Java Course Selected")
            case 3:
                print("C++ Course Selected")
            case _:
                print("Invalid course")

    case 2:
        print("Mathematics")
        choice2 = int(input("1 → Algebra\n2 → Calculus\n3 → Statistics\nEnter course: "))

        match choice2:
            case 1:
                print("Algebra Course Selected")
            case 2:
                print("Calculus Course Selected")
            case 3:
                print("Statistics Course Selected")
            case _:
                print("Invalid course")

    case 3:
        print("Communication")
        choice3 = int(input("1 → English\n2 → Presentation\n3 → Interview Skills\nEnter course: "))

        match choice3:
            case 1:
                print("English Course Selected")
            case 2:
                print("Presentation Course Selected")
            case 3:
                print("Interview Skills Course Selected")
            case _:
                print("Invalid course")

    case _:
        print("Invalid subject")