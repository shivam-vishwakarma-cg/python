
choice=int(input("Menu : \n1 → Search Book\n2 → Issue Book\n3 → Return Book\n4 → View Issued Books\n5 → Exit\nEnter choice: "))
match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")