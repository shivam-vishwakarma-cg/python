department=int(input("Menu : \n1 → General Medicine\n2 → Cardiology\n3 → Orthopedics\n4 → Pediatrics\n5 → Emergency\nEnter department: "))

match department:
    case 1:
        print("General Medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid Department")