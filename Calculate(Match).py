while True:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
    choice=int(input("Enter choice:"))
    match(choice):
        case 1:print(f"Addition={num1+num2}")
        case 2:print(f"Substraction={num1-num2}")
        case 3:print(f"Multiplication={num1*num2}")
        case 4:print(f"Division={num1/num2}")
    permission=input("Do you want to again try(y/n)")
    permission=permission.lower()
    if(permission!="y"):
        break