choice = int(input("1 → UPI\n2 → Card\n3 → Wallet\nEnter payment type: "))

match choice:
    case 1:
        print("UPI Payment")
        choice1 = int(input("1 → Scan QR\n2 → Enter UPI ID\nEnter option: "))

        match choice1:
            case 1:
                print("Scan QR Code")
            case 2:
                print("Enter UPI ID")
            case _:
                print("Invalid option")

    case 2:
        print("Card Payment")
        choice2 = int(input("1 → Credit Card\n2 → Debit Card\nEnter option: "))

        match choice2:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid option")

    case 3:
        print("Wallet Payment")
        choice3 = int(input("1 → Add Money\n2 → Pay Using Wallet\nEnter option: "))

        match choice3:
            case 1:
                print("Add Money to Wallet")
            case 2:
                print("Pay Using Wallet")
            case _:
                print("Invalid option")

    case _:
        print("Invalid payment type")
