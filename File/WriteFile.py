lst=[]
n=int(input("Enter size of list:"))
for i in range(0,n):
    lst.append((input("Enter data=")))
print(lst)

f1=open("memo.txt",mode="w")
f1.writelines(lst)
f1.close()