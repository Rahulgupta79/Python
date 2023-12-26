# Break-It is a Keyword which we use to break any loop statement and
#             in this case loop statement will not execute again

a=12
i=1
while(i<=a):
    if(i==6):
        break
    print(i)
    i+=1

    
print()
for j in range(1,a,1):
    if(j==8):
        break
    print(j)