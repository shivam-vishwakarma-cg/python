user=int(input("Enter user Type : "))
option=int(input("Enter option : "))
match user:
    case 1:
        match option:
            case 1:
                print("student courses")
            case 2:
                print("student marks")
            case 3:    
                print("student attendence")
    case 2:
        match option:
            case 1:
                print("teacher view courses")
            case 2:
                print("teacher can enter marks")
            case 3:    
                print("teacher view attendence")
        