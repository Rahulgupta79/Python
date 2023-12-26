from tkinter import *

root=Tk()
root.title("Registration Form")
root.geometry("600x600+400+10")

title=Label(root,text="Registration Form",font=("Algerian",30),bg="Yellow")
title.pack(side="top")

frame=Frame(root,bd=5,relief=RIDGE)
frame.place(x=0,y=50,width=600,height=550)

# Lable
nme=Label(frame,text="Name",font=("Times new roman",25))
nme.grid(row=3,column=2,sticky="W",padx=20,pady=10)
Roll=Label(frame,text="Roll No.",font=("Times new roman",25))
Roll.grid(row=4,column=2,sticky="W",padx=20,pady=10)
Gender=Label(frame,text="Gender",font=("Times new roman",25))
Gender.grid(row=5,column=2,sticky="W",padx=20,pady=10)

# Entry
nmeEntry=Entry(frame,width=25,font=("arial",15,"bold"))
nmeEntry.grid(row=3,column=3,sticky="W",padx=0,pady=20)
rollEntry=Entry(frame,width=25,font=("arial",15,"bold"))
rollEntry.grid(row=4,column=3,sticky="W",padx=0,pady=20)

# Radio Button
gender=StringVar()
male=Radiobutton(frame,text="male",font=("Times new roman",25),variable=gender,value="male")
male.grid(row=5,column=3,sticky="W")
female=Radiobutton(frame,text="female",font=("Times new roman",25),variable=gender,value="female")
female.grid(row=5,column=4,sticky="W")
gender.set("male")
# CheckBox
checkbox=Checkbutton(frame,text="Agree all terms & conditions",font=("calibri",15))
checkbox.grid(row=6,column=2,sticky="W")
# Submit Button
btn=Button(frame,text="Submit")
btn.place(x=250,y=350)

root.mainloop()