import pickle

lst=[]
n=int(input("Enter size of list:"))
for i in range(0,n):
    lst.append((input("Enter data=")))
print(lst)
p=open("demo.txt","w")
pickle.dump("lst","p")
p.flush()
print("Data insert successful")



# with open("demo.txt","w+")as p:
#     pickle.dump(lst,p)
#     p.flush()
