def prime(num1):
    p=0
    i=2
    while(i<=num1/2):
        if(num1%i==0):
            p+=1
            i+=1

    if(p>0):
        return 0
    else:
        return num1


num=int(input("Enter how much you want to prime number:"))
x=2
i=1
no=0
lst=[]
while(i<=num):
    no=prime(x)
    if(no!=0):
        lst.append(no)
    x+=1
    i+=1
  
print(lst)