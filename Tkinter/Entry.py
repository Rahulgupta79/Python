from tkinter import*

root=Tk()
en=Entry(root,width=30)
en.pack()
# Entry data likhte jate hai o data hide hote jata hai
# Text data likhiye o dikhai dete rahta hai kya kya likhe

def click():
    value=en.get()
    lbl=Label(root,text=value)
    # lbl=Label(root,text=en.get())
    lbl.pack()


Btn=Button(root,text=("Enter"),command=click,bg="#818181")
Btn.pack()



root.geometry("800x600")
root.title("Entry Block")
root.mainloop()