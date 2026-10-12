choice = int(input("1 → Starters\n2 → Main Course\n3 → Desserts\n4 → Drinks\nEnter category: "))

match choice:
    case 1:
        print("Starters")
        choice1 = int(input("1 → Soup\n2 → Spring Roll\n3 → Garlic Bread\nEnter item: "))

        match choice1:
            case 1:
                print("Soup Ordered")
            case 2:
                print("Spring Roll Ordered")
            case 3:
                print("Garlic Bread Ordered")
            case _:
                print("Invalid item")

    case 2:
        print("Main Course")
        choice2 = int(input("1 → Pizza\n2 → Pasta\n3 → Biryani\nEnter item: "))

        match choice2:
            case 1:
                print("Pizza Ordered")
            case 2:
                print("Pasta Ordered")
            case 3:
                print("Biryani Ordered")
            case _:
                print("Invalid item")

    case 3:
        print("Desserts")
        choice3 = int(input("1 → Ice Cream\n2 → Cake\n3 → Gulab Jamun\nEnter item: "))

        match choice3:
            case 1:
                print("Ice Cream Ordered")
            case 2:
                print("Cake Ordered")
            case 3:
                print("Gulab Jamun Ordered")
            case _:
                print("Invalid item")

    case 4:
        print("Drinks")
        choice4 = int(input("1 → Coffee\n2 → Tea\n3 → Juice\nEnter item: "))

        match choice4:
            case 1:
                print("Coffee Ordered")
            case 2:
                print("Tea Ordered")
            case 3:
                print("Juice Ordered")
            case _:
                print("Invalid item")

    case _:
        print("Invalid category")
