n=int(input("Enter a number="))
a=[]
while(n!=0):
    a.append(n%10)
    n//=10

print(a)
b=[]
i=0
while(i<len(a)):
    b.append((a[i])*(a[i]))
    i+=1
print(b)