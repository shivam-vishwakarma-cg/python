choose=int(input("""Enter signal :
1.red
2.yellow
3.green"""))
match choose:
    case 1:
        print("Stop")
    case 2:
        print("Wait")
    case 3:
        print("Go")
    case _:
        print("Invalid Signal")
        