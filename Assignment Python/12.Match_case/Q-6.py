choose=int(input("""1 → Electronics
2 → Clothing
3 → Books
4 → Grocery
5 → Exit"""))
match choose:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case _:
        print("exit")
        