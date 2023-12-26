f1=open("demo.txt",mode="r")
f2=open("memo.txt",mode="w")
# print(f1.readlines())
data=f1.readlines()
for line in data:
    f2.write(line)
f1.close()
f2.close()