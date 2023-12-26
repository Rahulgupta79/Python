from tkinter import*

root=Tk()
root.geometry("800x600")
root.title("Styling ")

lbl=Label(root,text="Welcome to Styling",relief=RIDGE,font=("time new roman",20,"bold"),bd=5)
lbl.pack()

ent=Entry(root,width=40,bg="yellow",fg="red")
ent.pack()

ent=Entry(root,width=40,show="*")#show attribute use for hide user data
ent.pack()

btn=Button(root,text="Click Now",bg="blue",fg="white",width=20,font=("Algerian",20),bd=6,activebackground="blue",activeforeground="white",cursor="hand2")
btn.pack()

root.mainloop()
# bg=background color
# fg=Foreground color 
# show=hide used input data
# activebackground/foreground =ye btn click karne pe bydefault white/black aata hai use change kar sakte hai
# cursor=ye button pe hand lane ke lia use kiya jata hai