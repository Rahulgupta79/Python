n=int(input("Enter a number="))
i=2
p=0
while(i<=n/2):
    if(n%i==0):
        p+=1
    i+=1
if(p>0):
    print("Not Prime=",n)
else:
    print("Prime number=",n)