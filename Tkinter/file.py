from tkinter import*
from tkinter import filedialog as fd
root=Tk()
root.title("Icon")
root.geometry("300x300")
fil=(("All","*.*"),("python","*.py"))
def Open():
    file=fd.askopenfile(title="Choose Rahul",filetypes=fil)
    fileName=file.name
    fileData=open(rf"{fileName}",mode="r").read()
    lbl.config(text=fileData)
lbl=Label(root)
lbl.pack()
btn=Button(root,text="Btn",command=Open)
btn.pack(side="bottom")
root.mainloop()