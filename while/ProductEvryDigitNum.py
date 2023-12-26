n=int(input("Enter a number:"))
mul=1
while(n>0):
    mul=mul*(n%10)
    n//=10

print("Product of Every digit of number=",mul)