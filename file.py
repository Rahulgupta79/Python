import PIL.Image as p
# a=int(input("Enter a number="))
# print(a)
# When we want save data to our permanent storage in this time  a word moving around our  mind that is Handling data
# types of storing data ->2
# Text file   / Binary file
# Mode file r/w/a/r+/w+/a+  text->t  binary->b
# cursor 
# f=open("C:\\Users\\rahul\\OneDrive\\Desktop\\pic.jpeg",mode="rb")
# name=input("Enter a name=")
# f.write(name)
# f.seek(2)#jump cursor to define place
# name=f.read()
# name=f.readline()
# name=f.readlines()
# print(f.tell())#Tells about character in file
# f.close()
img=p.open("C:\\Users\\rahul\\OneDrive\\Desktop\\pic.jpeg")
img.show()
img.close()