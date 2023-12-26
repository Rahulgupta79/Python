
class BalanceExceptionError(Exception):
    def __init__(self):
        print("Insufficient Balance",end="")

class AttemptExceptionError(Exception):
    def __init__(self):
        print("Your attempt will out of Range Your A/c will block for 1Hr")


attempt=1
def withdraw():
    saved_pin=7979
    balance=10000
    global attempt
    pin=int(input("Enter your PIN:"))
    if(saved_pin==pin):
        try:
            amt=int(input("Enter amount to withdraw:"))
            temp_bal=balance-amt
            if(temp_bal<1000):
                raise BalanceExceptionError
        except BalanceExceptionError as obj:
            print(obj)
        else:
            balance=balance-amt
        finally:
            print("Remaining Balance=",balance)
    else:
        ch=input("Continue to again(Y/N)")
        if(ch=='Y'or'y'):
            attempt+=1
            try:
                if(attempt==4):
                    raise AttemptExceptionError
            except AttemptExceptionError as obj:
                print(obj)
            else:
                    withdraw()
        else:
            print("Thanks For Visit !")
            return
print("Welcome to ATM")
withdraw()