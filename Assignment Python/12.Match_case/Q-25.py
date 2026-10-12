choice = int(input("Menu : \n1 → Regular\n2 → Premium\n3 → VIP\nEnter choice: "))

match choice:

    case 1:
        ticket = "Regular Ticket"

    case 2:
        ticket = "Premium Ticket"

    case 3:
        ticket = "VIP Ticket"

    case _:
        print("Invalid Choice")
        exit()

age = int(input("Enter age: "))

if age < 5:
    print("Free Entry")
else:
    print(ticket)