from tkinter import *
root=Tk()
root.title("Scroll Area")
root.geometry("600x500+350+120")

fr=Frame(root,relief=RIDGE,bd=3)
fr.place(x=100,y=100,width=160,height=205)

scr_x=Scrollbar(fr,orient=HORIZONTAL)
scr_x.pack(side=BOTTOM,fill=X)
scr_y=Scrollbar(fr,orient=VERTICAL)
scr_y.pack(side=RIGHT,fill=Y)

lst=Listbox(fr,font=("arial",15,"bold"))
lst.place(x=0,y=0)
l_list=["Student","College","Hospital","Block","Mohan","Rohan","Rahul","Rajvir","Abhishek"]
for i in l_list:
    lst.insert(END,i)


root.mainloop()