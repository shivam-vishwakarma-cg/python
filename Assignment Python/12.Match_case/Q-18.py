category = int(input("Enter category: "))

match category:
    case 1:
        product = int(input("Enter product: "))
        match product:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case 3:
                print("Headphones")
            case _:
                print("Invalid")

    case 2:
        product = int(input("Enter product: "))
        match product:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case 3:
                print("Shoes")
            case _:
                print("Invalid")

    case _:
        print("Invalid Category")