from tkinter import*
first=second=opr=None
class window:
    def __init__(self):
        root=Tk()
        root.title("Calculator")
        root.geometry("260x260")
        root.resizable(0,0)
        root.config(bg="black")

        # en=Entry(root,width=15,font=("arial",20),state="readonly")
        
        lbl=Label(root,text="",width=15,font=("arial",20))
        lbl.place(x=15,y=8)

        def clear():
            global first,second,opr
            lbl["text"]=""
            first=second=opr=None
            

        def show(digit):
            curVal=lbl["text"]
            newVal=curVal + str(digit)
            lbl["text"]=newVal
            # lbl.config(text=newVal)
   
        def operator(op):
            global first,opr
            first = int(lbl["text"])
            opr=op
            # print(opr)
            lbl["text"]=""

        def result():
            global first,second,opr
            second=int(lbl["text"])
            # print(second)
            match(opr):
                case "+":lbl["text"]=first+second
                case "-":lbl["text"]=first-second
                case "*":lbl["text"]=first*second
                case "/":
                    if(second==0):
                        lbl["text"]="Invalid"
                    else:
                        lbl["text"]=round(first/second,4)


        btn=Button(root,text=7,width=4,font=("arial",15),command=lambda:show(7),cursor="hand2")
        btn.place(x=16,y=60)
        btn=Button(root,text=8,width=4,font=("arial",15),command=lambda:show(8),cursor="hand2")
        btn.place(x=75,y=60)
        btn=Button(root,text=9,width=4,font=("arial",15),command=lambda:show(9),cursor="hand2")
        btn.place(x=135,y=60)
        btn=Button(root,text="+",width=4,font=("arial",15),command=lambda:operator("+"),cursor="hand2")
        btn.place(x=195,y=60)

        btn=Button(root,text=4,width=4,font=("arial",15),command=lambda:show(4),cursor="hand2")
        btn.place(x=16,y=110)
        btn=Button(root,text=5,width=4,font=("arial",15),command=lambda:show(5),cursor="hand2")
        btn.place(x=75,y=110)
        btn=Button(root,text=6,width=4,font=("arial",15),command=lambda:show(6),cursor="hand2")
        btn.place(x=135,y=110)
        btn=Button(root,text="-",width=4,font=("arial",15),command=lambda:operator("-"),cursor="hand2")
        btn.place(x=195,y=110)

        btn=Button(root,text=1,width=4,font=("arial",15),command=lambda:show(1),cursor="hand2")
        btn.place(x=16,y=160)
        btn=Button(root,text=2,width=4,font=("arial",15),command=lambda:show(2),cursor="hand2")
        btn.place(x=75,y=160)
        btn=Button(root,text=3,width=4,font=("arial",15),command=lambda:show(3),cursor="hand2")
        btn.place(x=135,y=160)
        btn=Button(root,text="x",width=4,font=("arial",15),command=lambda:operator("*"),cursor="hand2")
        btn.place(x=195,y=160)

        btn=Button(root,text="C",width=4,font=("arial",15),command=clear,cursor="hand2")
        btn.place(x=16,y=210)
        btn=Button(root,text=0,width=4,font=("arial",15),command=lambda:show(0),cursor="hand2")
        btn.place(x=75,y=210)
        btn=Button(root,text="=",width=4,font=("arial",15),command=result,cursor="hand2")
        btn.place(x=135,y=210)
        btn=Button(root,text="/",width=4,font=("arial",15),command=lambda:operator("/"),cursor="hand2")
        btn.place(x=195,y=210)


        root.mainloop()


pointer=window()

