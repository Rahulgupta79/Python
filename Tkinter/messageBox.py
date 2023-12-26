from tkinter import*
from tkinter import messagebox


root=Tk()
root.geometry("800x600")
root.title("TextBox")

def dp():
    messagebox.showinfo("rahul","maja aaya!")

btn=Button(root,text="Hello",command=dp)
btn.place(x=100,y=100)

def dp1():
    messagebox.showwarning("rahul","maja aaya!")
    
btn1=Button(root,text="Hello1",command=dp1)
btn1.place(x=100,y=200)

def dp2():
    messagebox.showerror("rahul","maja  nhi aaya!")
    
btn2=Button(root,text="Hello2",command=dp2)
btn2.place(x=100,y=300)
root.mainloop()
