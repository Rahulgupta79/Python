from tkinter import*
root=Tk()
root.title("Gui")#Title
root.geometry("800x400+100+80")#widthxheight+x+y
root.minsize(600,200)#It tells minimum size of window
root.maxsize(800,700)#It tells maximum size of window
nm=Label(root,text="Name")
nm.pack()
# nm.place(x=80,y=20)
# nm.grid(row=0,column=0)
nm=Label(root,text="Name")
nm.pack()
# nm.place(x=100,y=200)
# nm.grid(row=1,column=0)
nm=Label(root,text="Name")
nm.pack()
# nm.place(x=10,y=80)
# nm.place(x=100,y=200)
# nm.grid(row=2,column=0)