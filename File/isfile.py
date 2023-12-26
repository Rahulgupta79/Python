import os.path as j
name=input("Enter file Name=")
if(j.isfile(name)):
    print("File is Exists")
    f=open(name)
    f.close()
else:
    print("File doesn't Exist")