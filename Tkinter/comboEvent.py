from tkinter import*
from tkinter import ttk

root=Tk()
root.geometry("300x200")

def deo(event):
    print(op.get())
    if(op.get()!="Select"):
        en.config(state=NORMAL)

op=ttk.Combobox(root)
op["value"]=("Select","Male","Female")
op.current(0)
op.pack()
op.bind("<<ComboboxSelected>>",deo)

en=Entry(root,state=DISABLED)
en.pack()
root.mainloop()