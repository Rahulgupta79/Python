from tkinter import*
from tkinter import ttk


root=Tk()
root.geometry("800x600")
root.title("ListBox")

course=["rahul","rohan","mohan"]
lst=Listbox(root)
lst.place(x=100,y=50)
for i in course:
    lst.insert(END,i)

def show():
    cursor=lst.curselection()
    print(cursor)
    for i in cursor:
        print(lst.get(i))

btn=Button(root,text="show Data",command=show)
btn.place(x=300,y=50)

root.mainloop()