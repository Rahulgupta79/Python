n=input("Enter a name:")
num=int(input("Enter Repetation="))
count=0
def printer(num):
    if(count==num):
        return
    else:
        print(n)
        return printer(num-1)
printer(num)