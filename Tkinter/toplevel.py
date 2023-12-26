from tkinter import*
rot=Tk()
rot.title("demo")
rot.geometry("400x300")
b=""
def CF():
    root=Toplevel(rot)
    root.title("Temperature")
    root.geometry("300x180")
    cel=StringVar()
    frh=StringVar()
    
    def clear():
        global b
        cel.set(b)
        frh.set(b)

    def Convert():
        celsius=float(cel.get())
        result=(celsius*9/5)+32
        frh.set(round(result,2))

    lbl=Label(root,text="Celsius",font=("arial",15))
    lbl.place(x=60,y=50)
    Cel=Entry(root,font=("arial",15),width=8,textvariable=cel)
    Cel.place(x=180,y=50)

    lbl=Label(root,text="Fahrenheight",font=("arial",15))
    lbl.place(x=60,y=80)
    Frh=Entry(root,font=("arial",15),width=8,textvariable=frh,state="readonly")
    Frh.place(x=180,y=80)

    convert=Button(root,text="Converter",font=("Arial",12),cursor="hand2",command=Convert)
    convert.place(x=80,y=120)

    Clear=Button(root,text="Clear",font=("Arial",12),cursor="hand2",command=clear)
    Clear.place(x=180,y=120)

    root.mainloop()

Clear=Button(rot,text="Clear",font=("Arial",12),cursor="hand2")
Clear.place(x=180,y=120)
rot.mainloop()