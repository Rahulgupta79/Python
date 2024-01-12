n=int(input("Enter a number="))
def decending(n):
    print(n)
    if(n==1):
        print("Thanks for using!") 
    else:
        return[decending(n-1)]
    
decending(n)