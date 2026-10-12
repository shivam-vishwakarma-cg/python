choose=int(input("""enter your order 
1 → Pizza
2 → Burger
3 → Pasta
4 → Sandwich"""))
match choose:
    case 1:
        print("You Selected Pizza")
    case 2:
        print("You Selected Burger")
    case 3:
        print("You Selected pasta")
    case 4:
        print("You Selected Sandwich")
    case _:
        print("Invalid menu Choice")
