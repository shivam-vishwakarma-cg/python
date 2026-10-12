choice = int(input("1 → Flight\n2 → Train\n3 → Bus\nEnter transport: "))

match choice:
    case 1:
        print("Flight")
        choice1 = int(input("1 → Economy\n2 → Business\nEnter class: "))

        match choice1:
            case 1:
                print("Economy Class Selected")
            case 2:
                print("Business Class Selected")
            case _:
                print("Invalid option")

    case 2:
        print("Train")
        choice2 = int(input("1 → Sleeper\n2 → AC\nEnter class: "))

        match choice2:
            case 1:
                print("Sleeper Class Selected")
            case 2:
                print("AC Class Selected")
            case _:
                print("Invalid option")

    case 3:
        print("Bus")
        choice3 = int(input("1 → Ordinary\n2 → Volvo\nEnter bus type: "))

        match choice3:
            case 1:
                print("Ordinary Bus Selected")
            case 2:
                print("Volvo Bus Selected")
            case _:
                print("Invalid option")

    case _:
        print("Invalid transport")