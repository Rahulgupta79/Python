from tkinter import*
from tkinter.ttk import Combobox

root=Tk()
root.geometry("800x600")
root.title("DownList")

def show():
    print(gender.get())

gender=Combobox(root,font=("arial",12,"bold"))
gender["value"]=("html","java","css","py")
gender.place(x=300,y=100)
gender.set("select option")

btn=Button(root,text="Show Values",font=("arial",20,"bold"),command=show)
btn.place(x=300,y=200)
root.mainloop()

