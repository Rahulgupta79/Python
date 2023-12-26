from tkinter import *
root=Tk()
root.title("Registration Form")
root.geometry("600x570")
# Heading
head=Label(root,text="Registeration Form",font=("arial",30,"bold"),fg="red")
head.place(x=150,y=20)
# Data Label
name=Label(root,text="Name",font=("times new roman",15,"bold"))
age=Label(root,text="Age",font=("times new roman",15,"bold"))
phone_No=Label(root,text="Phone No",font=("times new roman",15,"bold"))
email_Id=Label(root,text="Email Id",font=("times new roman",15,"bold"))
name.place(x=100,y=150)
age.place(x=100,y=200)
phone_No.place(x=100,y=250)
email_Id.place(x=100,y=300)
# variable
name_data=StringVar()
age_data=StringVar()
phone_data=StringVar()
email_data=StringVar()
# Data Entry
name_Entry=Entry(root,width=35,font=("arial",12),textvariable=name_data)
age_Entry=Entry(root,width=35,font=("arial",12),textvariable=age_data)
phone_Entry=Entry(root,width=35,font=("arial",12),textvariable=phone_data)
email_Entry=Entry(root,width=35,font=("arial",12),textvariable=email_data)
name_Entry.place(x=200,y=150)
age_Entry.place(x=200,y=200)
phone_Entry.place(x=200,y=250)
email_Entry.place(x=200,y=300)
# Check Box
checkbox=Checkbutton(root,text="Agree for terms and Conditions",font=("arial",12))
checkbox.place(x=200,y=350)

# file


# Function
def display():
    print("Data Inserted Successful")
    Name=name_data.get()
    Age=age_data.get()
    Phone=phone_data.get()
    Email=email_data.get()
    
    with open("file.txt","w+") as f:
        f.write(Name)
        f.write(Age)
        f.write(Phone)
        f.write(Email)

def clear():
    name_data.set("")
    age_data.set("")
    phone_data.set("")
    email_data.set("")

def exitRoot():
    root.destroy()

# Register Button
register=Button(root,text="Register",font=("arial",15,"bold"),command=display)
clear=Button(root,text="Clear",font=("arial",15,"bold"),command=clear)
exit=Button(root,text="Exit",font=("arial",15,"bold"),command=exitRoot)
exit.place(x=450,y=450)
clear.place(x=350,y=450)
register.place(x=250,y=450)

root.mainloop()