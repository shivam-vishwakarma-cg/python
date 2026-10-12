choice = int(input("1 → Engine\n2 → Lights\n3 → Music\n4 → Navigation\nEnter choice: "))

match choice:
    case 1:
        print("Engine")
        choice1 = int(input("1 → Start\n2 → Stop\nEnter option: "))

        match choice1:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid option")

    case 2:
        print("Lights")
        choice2 = int(input("1 → Headlights\n2 → Indicators\n3 → Hazard Lights\nEnter option: "))

        match choice2:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid option")

    case 3:
        print("Music")
        choice3 = int(input("1 → Play\n2 → Pause\n3 → Next\n4 → Previous\nEnter option: "))

        match choice3:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Playing Next Song")
            case 4:
                print("Playing Previous Song")
            case _:
                print("Invalid option")

    case 4:
        print("Navigation")
        choice4 = int(input("1 → Start Navigation\n2 → Stop Navigation\nEnter option: "))

        match choice4:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid option")

    case _:
        print("Invalid choice")