device=int(input("Menu : \n1 → Light\n2 → Fan\n3 → AC\n4 → TV\nEnter device: "))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")