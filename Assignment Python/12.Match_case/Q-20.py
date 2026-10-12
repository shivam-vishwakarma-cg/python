a=int(input("Enter a : "))
b=int(input("Enter b : "))
oparation=input("Menu : \n+ Addtion\n- substraction\n* multiplication\n/ division\n% modulus\n//floor-division \nEnter your choice : ")

match oparation:
    case "+":
        print("Addition ",a+b)
    case "-":
        print("Substraction : ",a-b)
    case "*":
        print("multiplication : ",a*b)
    case "/":
        print("division : ",a/b)
    case "%":
        print("modulus : ",a%b)
    case "//":
        print("modulus : ",a//b)
    case _:
        print("invalid")