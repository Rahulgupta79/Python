from tkinter import*

root=Tk()
root.title("Gui Interface")
root.geometry("800x500")
lb=Label(root,text="Gupta Media",font=("times new roman",30))
# lb.pack(side=TOP)#By default it is on top top/bottom/left/right

lb1=Label(root,text="New String",font=("Algerian",15))
# lb1.grid(row=0,column=0)

lb1.place(x=100,y=100)
root.mainloop()