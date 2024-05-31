from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Voltage Divider")
root.geometry("280x280+20+20")
root.config(bg="gray20")
root.resizable(0,0)
#variables
Vin=StringVar()
R1=StringVar()
R2=StringVar()

def calculate():
    cvin=float(Vin.get())
    if op1.get()==op2.get()=="Ohm" or op1.get()==op2.get()=="K-Ohm" or op1.get()==op2.get()=="M-Ohm" :
        cr1=float(R1.get())
        cr2=float(R2.get())
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    elif op1.get()=="Ohm" and op2.get()=="K-Ohm":
        cr1=float(R1.get())
        cr2=float(R2.get())*1000
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    elif op1.get()=="K-Ohm" and op2.get()=="Ohm":
        cr1=float(R1.get())*1000
        cr2=float(R2.get())
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    elif op1.get()=="K-Ohm" and op2.get()=="M-Ohm":
        cr1=float(R1.get())*1000
        cr2=float(R2.get())*1000000
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    elif op1.get()=="M-Ohm" and op2.get()=="K-Ohm":
        cr1=float(R1.get())*1000000
        cr2=float(R2.get())*1000
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    elif op1.get()=="Ohm" and op2.get()=="M-Ohm":
        cr1=float(R1.get())
        cr2=float(R2.get())*1000000
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    elif op1.get()=="M-Ohm" and op2.get()=="Ohm":
        cr1=float(R1.get())*1000000
        cr2=float(R2.get())
        result=((cvin*cr2)/(cr1+cr2))
        voutlbl.config(text=format(result,'.3f'))
    else:
        voutlbl.config(text="Sys Error")
def Reset():
    Vin.set("")
    R1.set("")
    R2.set("")
    voutlbl.config(text="")

def Exit():
    root.destroy()


lframe=LabelFrame(root,text="Voltage Divider(Rahul Gupta)",bg="cyan")

vin=Entry(lframe,fg="gray20",textvariable=Vin,font=("times new roman",20,"bold"),width=10)
vin.grid(row=0,column=0,sticky=W,padx=10,pady=10)
vinlbl=Label(lframe,text="Vin",font=("times new roman",20,"bold"),bg="cyan")
vinlbl.grid(row=0,column=1,padx=5,pady=5)

r1=Entry(lframe,fg="gray20",width=10,textvariable=R1,font=("times new roman",20,"bold"),state=DISABLED)
r1.grid(row=1,column=0,sticky=W,padx=9,pady=5)

def deo1(event):
    if(op1.get()!="Select"):
        r1.config(state=NORMAL)

op1=ttk.Combobox(lframe,font=("times new roman",15,"bold"),width=7)
op1["value"]=("Select","Ohm","K-Ohm","M-Ohm")
op1.current(0)
op1.grid(row=1,column=1,padx=5,pady=5)
op1.bind("<<ComboboxSelected>>",deo1)

r2=Entry(lframe,fg="gray20",width=10,textvariable=R2,font=("times new roman",20,"bold"),state=DISABLED)
r2.grid(row=2,column=0,sticky=W,padx=9,pady=5)

def deo2(event):
    # print(op.get())
    if(op2.get()!="Select"):
        r2.config(state=NORMAL)

op2=ttk.Combobox(lframe,font=("times new roman",15,"bold"),width=7)
op2["value"]=("Select","Ohm","K-Ohm","M-Ohm")
op2.current(0)
op2.grid(row=2,column=1,padx=5,pady=5)
op2.bind("<<ComboboxSelected>>",deo2)


btn=Button(lframe,text="V-Out",command=calculate,font=("times new roman",15,"bold"),activebackground="gray20",activeforeground="cyan")
btn.grid(row=3,column=0,padx=20,pady=10)

voutlbl=Label(lframe,text="",font=("times new roman",20,"bold"),bg="cyan",)
voutlbl.grid(row=3,column=1,padx=5,pady=5)

rstbtn=Button(lframe,text="Reset",command=Reset,font=("times new roman",15,"bold"),activebackground="gray20",activeforeground="cyan")
rstbtn.grid(row=4,column=0,padx=20,pady=10)

closebtn=Button(lframe,text="Exit",command=Exit,font=("times new roman",15,"bold"),activebackground="gray20",activeforeground="cyan")
closebtn.grid(row=4,column=1,padx=20,pady=10)

lframe.pack()
root.mainloop()