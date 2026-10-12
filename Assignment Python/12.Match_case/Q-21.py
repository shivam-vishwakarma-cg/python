choice1=int(input("1.F\n2.C\nEter chocie : "))

match choice1:
    case 1:
        print("Celsius to Fahrenheit")
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f)
    case 2:
        print("Fahrenheit to Celsius")
        f = float(input("Enter temperature in F: "))
        c=(f-32)*5/9
        print(c)
