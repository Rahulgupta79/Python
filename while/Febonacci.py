num=int(input("Enter a number="))
x=0
y=1
z=0
while(z<=num-1):
    print(z,end="")
    x=y
    y=z
    z=x+y