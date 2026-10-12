choice=int(input("Menu : \n1 → Book Ticket\n2 → Cancel Ticket\n3 → Check PNR\n4 → Train Schedule\n5 → Exit\nEnter choice: "))

match choice:
    case 1:
        print("Ticket Booking Selected")
    case 2:
        print("Ticket Cancellation Selected")
    case 3:
        print("PNR Status Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")