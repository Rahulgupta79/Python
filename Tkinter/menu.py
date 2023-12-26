from tkinter import*

root=Tk()
root.title("Menubar")
root.geometry("600x500+120+120")
Mymenu=Menu(root)#Menu Object
root.config(menu=Mymenu)# Menu place to Window
SubmenuFile=Menu(Mymenu,tearoff=0)#it tells where we want to insert submenu if you not declare before then got a big error for it
SubmenuEdit=Menu(Mymenu,tearoff=0)
# Main menu
Mymenu.add_cascade(label="File",menu=SubmenuFile)
Mymenu.add_cascade(label="Edit",menu=SubmenuEdit)
# SubmenuFile
SubmenuFile.add_cascade(label="Create New File")
SubmenuFile.add_cascade(label="Save")
SubmenuFile.add_cascade(label="Save As")
# SubmenuEdit
SubmenuEdit.add_cascade(label="Undo")
SubmenuEdit.add_cascade(label="Redo")
SubmenuEdit.add_cascade(label="Cut")
SubmenuEdit.add_cascade(label="Paste")


root.mainloop()