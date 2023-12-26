# When we open a file we must to close it but close() method is not 100% 
# guarantee to close it then python give three types to close file
# f=open("demo.txt",mode="r+")
# print(f.read())
# f.close() 
# To close file in case file is not be close
# then you should try Exception Handling to close file


# try:
#     f=open("demo.txt",mode="r+")
#     print(f.read())
# finally:
#     f.close() 
#In this case file will closed 


# In other we use "with" statement to close file after perform our works
with open("demo.txt",mode="r+") as f:
    print(f.read())
