from tkinter import*
root=Tk()
root.title("Labal Frame")
root.geometry("600x300")
lbl=LabelFrame(root,text="Computer")
lbl.pack()
lb=Label(lbl,text="Rahul")
lb.pack()
root.mainloop()