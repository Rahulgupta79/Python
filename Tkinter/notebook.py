from tkinter import*
from tkinter import ttk
root=Tk()
root.title("NoteBook")
root.geometry("800x400")

n=ttk.Notebook(root)
tab1=Frame(n)
tab2=Frame(n)

n.add(tab1,text="Home")
n.add(tab2,text="Insert")
n.pack(expand=True,fill="both")

lbl=Label(tab1,text="This is first tab").place(x=10,y=10)
root.mainloop()