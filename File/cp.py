f1=open("C:\\Users\\rahul\\OneDrive\\Desktop\\pic.jpeg",mode="rb")
f2=open("C:\\Users\\rahul\\OneDrive\\Desktop\\jp.jpeg",mode="wb")
data=f1.readlines()
for line in data:
    f2.write(line)

f1.close()
f2.close()