choose=int(input("""1.sunny
2.rainy
3.cloudy
4.snowy"""))
match choose:
    case 1:
        print("Wear sunglasses")
    case 2:
        print("Carry an umbrella")
    case 3:
        print("Weather may change")
    case 4:
        print("Wear warm clothes")
    case _:
        print("exit")
        