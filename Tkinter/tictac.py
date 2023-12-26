from tkinter import*
root=Tk()
root.title("TicTac")
root.geometry("200x280")
root.resizable(0,0)
c=1
def tictac(b):
    global c
    c+=1
    if(c%2==0):
        if(b["text"]==""):
            b["text"]="O"
    else:
        if(b["text"]==""):
            b["text"]="X"
    
    pl1="Player 1  Winner"
    pl2="Player 2  Winner"


    if(b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O"):
        lbl["text"]=pl1
    elif(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        lbl["text"]=pl2

    elif(b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O"):
        lbl["text"]=pl1
    elif(b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
        lbl["text"]=pl2

    elif(b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O"):
        lbl["text"]=pl1
    elif(b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
        lbl["text"]=pl2

    elif(b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O"):
        lbl["text"]=pl1
    elif(b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
        lbl["text"]=pl2

    elif(b2["text"]=="O" and b1["text"]=="O" and b3["text"]=="O"):
        lbl["text"]=pl1
    elif(b2["text"]=="X" and b1["text"]=="X" and b3["text"]=="X"):
        lbl["text"]=pl2

    elif(b2["text"]=="O" and b3["text"]=="O" and b1["text"]=="O"):
        lbl["text"]=pl1
    elif(b2["text"]=="X" and b3["text"]=="X" and b1["text"]=="X"):
        lbl["text"]=pl2
    
    elif(b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        lbl["text"]=pl1
    elif(b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        lbl["text"]=pl2

    elif(b3["text"]=="O" and b2["text"]=="O" and b1["text"]=="O"):
        lbl["text"]=pl1
    elif(b3["text"]=="X" and b2["text"]=="X" and b1["text"]=="X"):
        lbl["text"]=pl2

    elif(b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
        lbl["text"]=pl1
    elif(b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        lbl["text"]=pl2
    
    elif(b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O"):
        lbl["text"]=pl1
    elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
        lbl["text"]=pl2

    elif(b4["text"]=="O" and b1["text"]=="O" and b7["text"]=="O"):
        lbl["text"]=pl1
    elif(b4["text"]=="X" and b1["text"]=="X" and b7["text"]=="X"):
        lbl["text"]=pl2

    elif(b4["text"]=="O" and b7["text"]=="O" and b1["text"]=="O"):
        lbl["text"]=pl1
    elif(b4["text"]=="X" and b7["text"]=="X" and b1["text"]=="X"):
        lbl["text"]=pl2
    
    elif(b5["text"]=="O" and b2["text"]=="O" and b8["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b2["text"]=="X" and b8["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b8["text"]=="O" and b2["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b8["text"]=="X" and b2["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b4["text"]=="O" and b6["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b4["text"]=="X" and b6["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b6["text"]=="O" and b2["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b6["text"]=="X" and b2["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b1["text"]=="O" and b9["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b1["text"]=="X" and b9["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b9["text"]=="O" and b1["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b9["text"]=="X" and b1["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b3["text"]=="O" and b7["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b3["text"]=="X" and b7["text"]=="X"):
        lbl["text"]=pl2

    elif(b5["text"]=="O" and b7["text"]=="O" and b3["text"]=="O"):
        lbl["text"]=pl1
    elif(b5["text"]=="X" and b7["text"]=="X" and b3["text"]=="X"):
        lbl["text"]=pl2

    elif(b6["text"]=="O" and b5["text"]=="O" and b4["text"]=="O"):
        lbl["text"]=pl1
    elif(b6["text"]=="X" and b5["text"]=="X" and b4["text"]=="X"):
        lbl["text"]=pl2

    elif(b6["text"]=="O" and b4["text"]=="O" and b5["text"]=="O"):
        lbl["text"]=pl1
    elif(b6["text"]=="X" and b4["text"]=="X" and b5["text"]=="X"):
        lbl["text"]=pl2

    elif(b6["text"]=="O" and b3["text"]=="O" and b9["text"]=="O"):
        lbl["text"]=pl1
    elif(b6["text"]=="X" and b3["text"]=="X" and b9["text"]=="X"):
        lbl["text"]=pl2

    elif(b6["text"]=="O" and b9["text"]=="O" and b3["text"]=="O"):
        lbl["text"]=pl1
    elif(b6["text"]=="X" and b9["text"]=="X" and b3["text"]=="X"):
        lbl["text"]=pl2

    elif(b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O"):
        lbl["text"]=pl1
    elif(b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
        lbl["text"]=pl2

    elif(b7["text"]=="O" and b9["text"]=="O" and b8["text"]=="O"):
        lbl["text"]=pl1
    elif(b7["text"]=="X" and b9["text"]=="X" and b8["text"]=="X"):
        lbl["text"]=pl2

    elif(b7["text"]=="O" and b4["text"]=="O" and b1["text"]=="O"):
        lbl["text"]=pl1
    elif(b7["text"]=="X" and b4["text"]=="X" and b1["text"]=="X"):
        lbl["text"]=pl2

    elif(b7["text"]=="O" and b1["text"]=="O" and b4["text"]=="O"):
        lbl["text"]=pl1
    elif(b7["text"]=="X" and b1["text"]=="X" and b4["text"]=="X"):
        lbl["text"]=pl2

    elif(b7["text"]=="O" and b5["text"]=="O" and b3["text"]=="O"):
        lbl["text"]=pl1
    elif(b7["text"]=="X" and b5["text"]=="X" and b3["text"]=="X"):
        lbl["text"]=pl2

    elif(b7["text"]=="O" and b3["text"]=="O" and b5["text"]=="O"):
        lbl["text"]=pl1
    elif(b7["text"]=="X" and b3["text"]=="X" and b5["text"]=="X"):
        lbl["text"]=pl2

    elif(b8["text"]=="O" and b5["text"]=="O" and b2["text"]=="O"):
        lbl["text"]=pl1
    elif(b8["text"]=="X" and b5["text"]=="X" and b2["text"]=="X"):
        lbl["text"]=pl2

    elif(b8["text"]=="O" and b2["text"]=="O" and b5["text"]=="O"):
        lbl["text"]=pl1
    elif(b8["text"]=="X" and b2["text"]=="X" and b5["text"]=="X"):
        lbl["text"]=pl2

    elif(b8["text"]=="O" and b7["text"]=="O" and b9["text"]=="O"):
        lbl["text"]=pl1
    elif(b8["text"]=="X" and b7["text"]=="X" and b9["text"]=="X"):
        lbl["text"]=pl2

    elif(b8["text"]=="O" and b9["text"]=="O" and b7["text"]=="O"):
        lbl["text"]=pl1
    elif(b8["text"]=="X" and b9["text"]=="X" and b7["text"]=="X"):
        lbl["text"]=pl2

    elif(b9["text"]=="O" and b5["text"]=="O" and b1["text"]=="O"):
        lbl["text"]=pl1
    elif(b9["text"]=="X" and b5["text"]=="X" and b1["text"]=="X"):
        lbl["text"]=pl2

    elif(b9["text"]=="O" and b1["text"]=="O" and b5["text"]=="O"):
        lbl["text"]=pl1
    elif(b9["text"]=="X" and b1["text"]=="X" and b5["text"]=="X"):
        lbl["text"]=pl2

    elif(b9["text"]=="O" and b6["text"]=="O" and b3["text"]=="O"):
        lbl["text"]=pl1
    elif(b9["text"]=="X" and b6["text"]=="X" and b3["text"]=="X"):
        lbl["text"]=pl2

    elif(b9["text"]=="O" and b3["text"]=="O" and b6["text"]=="O"):
        lbl["text"]=pl1
    elif(b9["text"]=="X" and b3["text"]=="X" and b6["text"]=="X"):
        lbl["text"]=pl2

    elif(b9["text"]=="O" and b8["text"]=="O" and b7["text"]=="O"):
        lbl["text"]=pl1
    elif(b9["text"]=="X" and b8["text"]=="X" and b7["text"]=="X"):
        lbl["text"]=pl2

    elif(b9["text"]=="O" and b7["text"]=="O" and b8["text"]=="O"):
        lbl["text"]=pl1
    elif(b9["text"]=="X" and b7["text"]=="X" and b8["text"]=="X"):
        lbl["text"]=pl2


b1=Button(root,width=8,height=4,command=lambda:tictac(b1))
b1.grid(row=0,column=0)
b2=Button(root,width=8,height=4,command=lambda:tictac(b2))
b2.grid(row=0,column=1)
b3=Button(root,width=8,height=4,command=lambda:tictac(b3))
b3.grid(row=0,column=2)

b4=Button(root,width=8,height=4,command=lambda:tictac(b4))
b4.grid(row=1,column=0)
b5=Button(root,width=8,height=4,command=lambda:tictac(b5))
b5.grid(row=1,column=1)
b6=Button(root,width=8,height=4,command=lambda:tictac(b6))
b6.grid(row=1,column=2)

b7=Button(root,width=8,height=4,command=lambda:tictac(b7))
b7.grid(row=2,column=0)
b8=Button(root,width=8,height=4,command=lambda:tictac(b8))
b8.grid(row=2,column=1)
b9=Button(root,width=8,height=4,command=lambda:tictac(b9))
b9.grid(row=2,column=2)

lbl=Label(root,text="",font=("Sanserif",13,"bold"))
lbl.grid(rows=3,columnspan=3)

def Rest():
    global c
    c=0
    lbl["text"]=""
    b1["text"]=""
    b2["text"]=""
    b3["text"]=""
    b4["text"]=""
    b5["text"]=""
    b6["text"]=""
    b7["text"]=""
    b8["text"]=""
    b9["text"]=""

Reset=Button(root,font=("Arial",12,"bold"),text="Reset",command=lambda:Rest())
Reset.grid(row=4,column=2)
Reset.place(x=70,y=240)
root.mainloop()