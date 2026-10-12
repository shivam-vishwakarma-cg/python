choice = int(input("Menu : \n1 → Start Exam\n2 → View Result\n3 → Exit\nEnter choice: "))

match choice:

    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result")

    case 3:
        print("Exit")

    case _:
        print("Invalid Choice")