choose=int(input("""1 → Morning Show
2 → Afternoon Show
3 → Evening Show
4 → Night Show"""))
match choose:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("Invalid Input")
        