Student_DB={}
while True:
    line=input("Enter a key & value and seperate by commma to exit press q=")
    if(line=='q'):
        break
    else:
        key,value=line.split(',')
        Student_DB.update({key:value})
    
for x,y in Student_DB.items():
    print(x,y)

data=input("Enter key:")
if data in Student_DB:
    print("Key=",data,"Value=",Student_DB[data])
else:
    print("Key is not found")

# Dictionary is set of key and values which is un-ordered and indexed by key
# In dictionary index of array which is 0,1,2,3... is changed with key 
