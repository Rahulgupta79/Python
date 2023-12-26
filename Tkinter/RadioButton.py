from tkinter import*
root=Tk()
root.title("Rahul")
root.geometry("600x400")#width x height + X + Y(co-ordinate)

def Gen():
    print(Gender.get())

Gender=StringVar()#It is a variable
male=Radiobutton(root,text="Male",variable=Gender,value="male")
male.place(x=100,y=50)
Gender.set("male")
female=Radiobutton(root,text="Female",variable=Gender,value="female")
female.place(x=200,y=50)

btn=Button(root,text="Click",command=Gen)
btn.place(x=400,y=50)

root.mainloop()#It helps to stable Gui Frame which we create