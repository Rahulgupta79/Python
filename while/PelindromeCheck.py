num=int(input("Enter a number="))
org=num
rev=0
while(num>0):
    rev=rev*10+num%10
    num//=10
print("Reverse number=",rev)
if(org==rev):
    print("Pelindrome Number=",org)
else:
    print("Not Pelindrome=",rev)