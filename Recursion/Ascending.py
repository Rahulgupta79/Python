n=int(input("Enter a number="))
i=1
def ascending(i):
    if(i==n+1):
        return
    else:
        print(i)
        return[ascending(i+1)]
ascending(i)