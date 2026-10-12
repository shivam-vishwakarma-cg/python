choice2=int(input("menu : \n1 → Kilometers to Meters\n2 → Meters to Kilometers\n3 → Kilograms to Grams\n4 → Grams to Kilograms"))
value=float(input("Enter value : "))

match choice2:
    case 1:
     
        print("in meters : ",value*1000)
    case 2:
       print("in m",value/1000)
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid choice")