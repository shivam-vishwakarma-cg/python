choice = int(input("1 → Start Game\n2 → Load Game\n3 → Settings\n4 → Exit\nEnter choice: "))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        print("Settings")
        choice1 = int(input("1 → Sound\n2 → Graphics\n3 → Controls\nEnter option: "))
        match choice1:
            case 1:
                print("Sound Settings")
            case 2:
                print("Graphics Settings")
            case 3:
                print("Controls Settings")
            case _:
                print("Invalid option")

    case 4:
        print("Exiting Game")

    case _:
        print("Invalid choice")