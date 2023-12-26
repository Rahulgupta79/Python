from tkinter import*

root=Tk()
root.geometry("800x600")
root.title("Button")

def click():
    lbl=Label(root,text=("Welcome Rahul jii"),font=("Algerian",25))
    lbl.pack()

btn=Button(root,text="Click Here",font=("Calibari",15),command=click)
btn.pack(side="bottom")



root.mainloop()