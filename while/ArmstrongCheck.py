n=int(input("Enter a number="))
org=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n//=10

if(sum==org):
    print("Number is armstrong=",org)
else:
    print("Number is not armstrong=",org)