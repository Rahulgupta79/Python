a=int(input("Enter a number="))
b=int(input("Enter a number="))
c=int(input("Enter a number="))
if((a<b and a>c)or(a<c and a>b)):
    print("Middle=",a)
elif((b>a and b<c)or(b>c and b<a)):
    print("Middle=",b)
else:
    print("Middle=",c)

'''
Enter a number=12
Enter a number=23
Enter a number=34
Middle= 23
'''