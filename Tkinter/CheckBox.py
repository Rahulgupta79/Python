from tkinter import*

root=Tk()
root.geometry("600x400")
root.title("CheckBox")

def CheckIt():
    print(Check_Value.get())

Check_Value=IntVar()
checkbox=Checkbutton(root,variable=Check_Value,onvalue=1,offvalue=0,text="Read terms & Condition")
checkbox.place(x=50,y=50)
Check_Value.set("0")#By default value of checkBox

btn=Button(root,text="Click",command=CheckIt)
btn.place(x=320,y=50)


root.mainloop()