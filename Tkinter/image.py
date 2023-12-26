from tkinter import*
root=Tk()
root.title("Icon")
root.geometry("300x300")
# root.iconbitmap("C:/Users/rahul/OneDrive/Desktop/Coding/Python/Tkinter/ins.ico")


img=PhotoImage(name="nme",file="C:/Users/rahul/OneDrive/Desktop/Coding/Python/Tkinter/apple.png")

lbl=Label(root,image=img)
lbl.pack()
root.mainloop()