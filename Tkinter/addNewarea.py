from tkinter import*
root=Tk()
root.geometry("400x400")

def BT():
    lbl=Label(root,text="Name")
    lbl.grid(row=0,column=0)
    Name=Entry(root)
    Name.grid(row=0,column=1)
btn=Button(root,text="Click",command=BT)
btn.grid(row=1,column=3)
root.mainloop()