
f=open('demo.txt',mode='r')
name=f.read()
print(name)
print("Filename is:",f.name)
print("Encoding name is:",f.encoding)
f.close()
print("File closed or not:",f.closed)
print("File mode is:",f.mode)

# f=open('demo.txt',mode='r')
# print(f.tell()) 
# #It tells cursor position of pointer
# print(f.read(3)) 
# #It tells how much character you want to read
# print(f.tell())
# f.seek(5) 
# #It sets cursor position as we want 
# print(f.read(5))
# print(f.tell())

# t=open("demo.txt",mode="r")
# # It tells that we take any name of file Handler 
# print(t.read())
