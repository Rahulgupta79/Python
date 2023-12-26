num1=int(input("Enter a number="))
num2=int(input("Enter a number="))
try:
    result=num1/num2
except ZeroDivisionError:
    print("Division by Zero is not Possible")
else:
    print("Division=",result)
    print("Addition=",num1+num2)
finally:
    print("Substract=",num1-num2)