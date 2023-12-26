from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk,filedialog
import mysql.connector
import pandas

# Main Window
root=Tk()
root.title("Adminstrator Login of Student Management System")
root.geometry("1360x750+0+0")
root.resizable(0,0)

# Adminstrator Variable
Name=StringVar()
Email=StringVar()
Gender=StringVar()
Phone=StringVar()
Username=StringVar()
Password=StringVar()

# Login Panel
UsernameN=StringVar()
PasswordN=StringVar()

# SearchPanel
SearchBox=StringVar()

# Student Variable
SregisterId=StringVar()
Sname=StringVar()
Sroll=StringVar()
Ssubject=StringVar()
Semail=StringVar()
Sdob=StringVar()
Sstate=StringVar()
Sdistrict=StringVar()
Sgender=StringVar()
Scaste=StringVar()
Snationality=StringVar()
Snumber=StringVar()

# UserWindow Function
def UserWindow():

    userWindow=Toplevel(root)
    userWindow.title("Adminstrator Login of Student Management System")
    userWindow.geometry("1360x750+0+0")
    userWindow.resizable(0,0)

    def exportData():
        url=filedialog.asksaveasfilename(defaultextension=".csv")
        lst=[]
        index=StudentTable.get_children()
        for data in index:
            ct=StudentTable.item(data)
            datalist=ct["values"]
            lst.append(datalist)
        Table=pandas.DataFrame(lst,columns=["Registration_ID","Name","Roll","Subject","Email","DOB","State","District","Gender","Caste","Nationality","Mobile_No"])
        Table.to_csv(url,index=False)
        messagebox.showinfo("Exported","Data Change into Spredsheet and Saved Successfully")

    def updatePanel():
        UpdatePanel=Toplevel(userWindow)
        UpdatePanel.title("Update Data")
        UpdatePanel.geometry("600x560+120+10")
        UpdatePanel.resizable(0,0)

        def updateData():
            if("@gmail.com" in Semail.get() and len(Snumber.get())==10):
                try:
                    conn=mysql.connector.connect(user="root",password="Mysql@123",host="localhost",port=3306,database="StudentManagement")
                except:
                    messagebox.showwarning("Student Database","Database Not Found")
                else:
                    cur=conn.cursor()
                    sql="UPDATE STUDENT SET SName=%s,SRoll=%s,SSubject=%s,SEmail=%s,SDOB=%s,SState=%s,SDistrict=%s,SGender=%s,SCaste=%s,SNationality=%s,SNumber=%s WHERE Registation_ID=%s"
                    cur.execute(sql,(SUName.get(),SURoll.get(),SUSubject.get(),SUEmail.get(),SUDob.get(),SUState.get(),SUDistrict.get(),SUGenderBox.get(),SUCasteBox.get(),SUNationalityBox.get(),SUNumber.get(),SURegisterId.get()))
                    conn.commit()
                    showData()
                    conn.close()
                    messagebox.showinfo("Updated",f"Data has been Updated\n Registation_ID={SURegisterId.get()}")
                    UpdatePanel.destroy()
            else:
                messagebox.showerror("Fields are not proper","Email_Id or Phone_No not Proper",parent=UpdatePanel)

        UpdateFrame=Frame(UpdatePanel)
        UpdateFrame.pack()
        SRegisterId=Label(UpdateFrame,text="Registration Id:",font=("Arial",15,"bold"))
        SRegisterId.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        SURegisterId=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SURegisterId.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        SName=Label(UpdateFrame,text="Student Name:",font=("Arial",15,"bold"))
        SName.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        SUName=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SUName.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        SRoll=Label(UpdateFrame,text="Roll:",font=("Arial",15,"bold"))
        SRoll.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        SURoll=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SURoll.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        SSubject=Label(UpdateFrame,text="Subject:",font=("Arial",15,"bold"))
        SSubject.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        SUSubject=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SUSubject.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        SEmail=Label(UpdateFrame,text="Student Email:",font=("Arial",15,"bold"))
        SEmail.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        SUEmail=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SUEmail.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        SDob=Label(UpdateFrame,text="Dob:",font=("Arial",15,"bold"))
        SDob.grid(row=5,column=0,padx=5,pady=5,sticky=W)
        SUDob=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SUDob.grid(row=5,column=1,padx=5,pady=5,sticky=W)
        SState=Label(UpdateFrame,text="State:",font=("Arial",15,"bold"))
        SState.grid(row=6,column=0,padx=5,pady=5,sticky=W)
        # SUState=Entry(UpdateFrame,font=("Arial",15,"bold"),width=25)
        # SUState.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        SUState=ttk.Combobox(UpdateFrame,font=("Arial",12,"bold"),state="readonly",width=28)
        SUState["value"]=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
        SUState.current(0)
        SUState.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        SDistrict=Label(UpdateFrame,text="District:",font=("Arial",15,"bold"))
        SDistrict.grid(row=7,column=0,padx=5,pady=5,sticky=W)
        SUDistrict=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SUDistrict.grid(row=7,column=1,padx=5,pady=5,sticky=W)
        SGender=Label(UpdateFrame,text="Gender:",font=("Arial",15,"bold"))
        SGender.grid(row=8,column=0,sticky=W)    
        SUGenderBox=ttk.Combobox(UpdateFrame,font=("Arial",15,"bold"),state="readonly",width=8)
        SUGenderBox["value"]=("Male","Female","Transgender")
        SUGenderBox.current(0)
        SUGenderBox.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        SCaste=Label(UpdateFrame,text="Caste:",font=("Arial",15,"bold"))
        SCaste.grid(row=9,column=0,padx=5,pady=5,sticky=W)
        SUCasteBox=ttk.Combobox(UpdateFrame,font=("Arial",12,"bold"),state="readonly",width=8)
        SUCasteBox["value"]=("General","BC-1","BC-2","EBC","SC","ST")
        SUCasteBox.current(0)
        SUCasteBox.grid(row=9,column=1,padx=5,pady=5,sticky=W)
        SNationality=Label(UpdateFrame,text="Nationality:",font=("Arial",15,"bold"))
        SNationality.grid(row=10,column=0,padx=5,pady=5,sticky=W)
        SUNationalityBox=ttk.Combobox(UpdateFrame,font=("Arial",12,"bold"),state="readonly",width=8)
        SUNationalityBox["value"]=("India","Nepal","China","USA","Brazil","Russia","Israel")
        SUNationalityBox.current(0)
        SUNationalityBox.grid(row=10,column=1,padx=5,pady=5,sticky=W)
        SNumber=Label(UpdateFrame,text="Mobile No:",font=("Arial",15,"bold"))
        SNumber.grid(row=11,column=0,padx=5,pady=5,sticky=W)
        SUNumber=Entry(UpdateFrame,font=("Arial",15,"bold"),bd=3,width=25)
        SUNumber.grid(row=11,column=1,padx=5,pady=5,sticky=W)

        SUpdate=Button(UpdateFrame,text="Update Now",font=("Arial",18,"bold"),bd=5,activebackground="blue",activeforeground="white",command=updateData)
        SUpdate.grid(row=12,column=1,columnspan=2,padx=5,pady=5,sticky=W)

        index=StudentTable.focus()
        Ct=StudentTable.item(index)
        data=Ct["values"]
        SURegisterId.insert(0,data[0])
        SUName.insert(0,data[1])
        SURoll.insert(0,data[2])
        SUSubject.insert(0,data[3])
        SUEmail.insert(0,data[4])
        SUDob.insert(0,data[5])
        SUState.insert(0,data[6])
        SUDistrict.insert(0,data[7])
        SUGenderBox.insert(0,data[8])
        SUCasteBox.insert(0,data[9])
        SUNationalityBox.insert(0,data[10])
        SUNumber.insert(0,data[11])

        UpdatePanel.mainloop()

    def deleteData():
        try:
            conn=mysql.connector.connect(user="root",password="Mysql@123",host="localhost",port=3306,database="StudentManagement")
        except:
            messagebox.showwarning("Student Database","Database Not Found")
        else:
            cur=conn.cursor()
            index=StudentTable.focus()
            Ct=StudentTable.item(index)
            regID=Ct["values"][0]
            sql="DELETE FROM STUDENT WHERE Registation_ID='{}' ".format(regID)
            cur.execute(sql)
            conn.commit()
            showData()
            conn.close()
            messagebox.showinfo("Deleted",f"Data has been deleted\n Registation_ID={regID}")

    def addmissionPanel():
        AddmissionPanel=Toplevel(userWindow)
        AddmissionPanel.title("Admission Student")
        AddmissionPanel.geometry("600x600+120+10")
        AddmissionPanel.resizable(0,0)

        def Ssubmit():
            if(SregisterId.get()=="" or Sname.get()=="" or Sroll.get()=="" or Ssubject.get()=="" or
            Semail.get()=="" or Sdob.get()=="" or Sstate.get()=="" or Sdistrict.get()=="" or
            Sgender.get()=="" or Scaste.get()=="" or Snationality.get()=="" or Snumber.get()==""):
                messagebox.showerror("Student records Blank","All fields are mendatory")
                AddmissionPanel.destroy()
            else:
                if("@gmail.com" in Semail.get() and len(Snumber.get())==10):
                    try:
                        conn=mysql.connector.connect(user="root",password="Mysql@123",host="localhost",port=3306,database="StudentManagement")
                        cur=conn.cursor()
                        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (SregisterId.get(), Sname.get(), Sroll.get(), Ssubject.get(),
                                    Semail.get(), Sdob.get(), Sstate.get(), Sdistrict.get(),
                                    Sgender.get(), Scaste.get(), Snationality.get(), Snumber.get()))
                    except:
                        messagebox.showwarning("Student Database","Duplicate Entry")
                    else:
                        conn.commit()
                        showData()
                        conn.close()
                        messagebox.showinfo("Successful","Data Inserted")
                        AddmissionPanel.destroy()
                    finally:
                        SregisterId.set("")
                        Sname.set("")
                        Sroll.set("")
                        Ssubject.set("")
                        Semail.set("")
                        Sdob.set("")
                        Sstate.set("")
                        Sdistrict.set("")
                        Sgender.set("")
                        Scaste.set("")
                        Snationality.set("")
                        Snumber.set("")
                else:
                    messagebox.showerror("Fields are not proper","Email_Id or Phone_No not Proper",parent=AddmissionPanel)

        addmissionFrame=Frame(AddmissionPanel)
        addmissionFrame.pack()

        SRegisterId=Label(addmissionFrame,text="Registration Id:",font=("Arial",15,"bold"))
        SRegisterId.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        SRegisterId=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=SregisterId)
        SRegisterId.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        SName=Label(addmissionFrame,text="Student Name:",font=("Arial",15,"bold"))
        SName.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        SName=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=Sname)
        SName.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        SRoll=Label(addmissionFrame,text="Roll:",font=("Arial",15,"bold"))
        SRoll.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        SRoll=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=Sroll)
        SRoll.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        SSubject=Label(addmissionFrame,text="Subject:",font=("Arial",15,"bold"))
        SSubject.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        SSubject=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=Ssubject)
        SSubject.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        SEmail=Label(addmissionFrame,text="Student Email:",font=("Arial",15,"bold"))
        SEmail.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        SEmailEn=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=Semail)
        SEmailEn.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        SDob=Label(addmissionFrame,text="Dob:",font=("Arial",15,"bold"))
        SDob.grid(row=5,column=0,padx=5,pady=5,sticky=W)
        SDobEn=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=Sdob)
        SDobEn.grid(row=5,column=1,padx=5,pady=5,sticky=W)
        SState=Label(addmissionFrame,text="State:",font=("Arial",15,"bold"))
        SState.grid(row=6,column=0,padx=5,pady=5,sticky=W)
        # SStateEn=Entry(addmissionFrame,font=("Arial",15,"bold"),width=25,textvariable=Sstate)
        # SStateEn.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        SStateEn=ttk.Combobox(addmissionFrame,font=("Arial",12,"bold"),state="readonly",width=28,textvariable=Sstate)
        SStateEn["value"]=("Select","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
        SStateEn.current(0)
        SStateEn.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        SDistrict=Label(addmissionFrame,text="District:",font=("Arial",15,"bold"))
        SDistrict.grid(row=7,column=0,padx=5,pady=5,sticky=W)
        SDistrictEn=Entry(addmissionFrame,font=("Arial",12,"bold"),bd=3,width=25,textvariable=Sdistrict)
        SDistrictEn.grid(row=7,column=1,padx=5,pady=5,sticky=W)
        SGender=Label(addmissionFrame,text="Gender:",font=("Arial",15,"bold"))
        SGender.grid(row=8,column=0,sticky=W)    
        SGenderBox=ttk.Combobox(addmissionFrame,font=("Arial",12,"bold"),state="readonly",width=8,textvariable=Sgender)
        SGenderBox["value"]=("Male","Female","Transgender")
        SGenderBox.current(0)
        SGenderBox.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        SCaste=Label(addmissionFrame,text="Caste:",font=("Arial",15,"bold"))
        SCaste.grid(row=9,column=0,padx=5,pady=5,sticky=W)
        SCasteBox=ttk.Combobox(addmissionFrame,font=("Arial",12,"bold"),state="readonly",width=8,textvariable=Scaste)
        SCasteBox["value"]=("General","BC-1","BC-2","EBC","SC","ST")
        SCasteBox.current(0)
        SCasteBox.grid(row=9,column=1,padx=5,pady=5,sticky=W)
        SNationality=Label(addmissionFrame,text="Nationality:",font=("Arial",15,"bold"))
        SNationality.grid(row=10,column=0,padx=5,pady=5,sticky=W)
        SNationalityBox=ttk.Combobox(addmissionFrame,font=("Arial",12,"bold"),state="readonly",width=8,textvariable=Snationality)
        SNationalityBox["value"]=("India","Nepal","China","USA","Brazil","Russia","Israel")
        SNationalityBox.current(0)
        SNationalityBox.grid(row=10,column=1,padx=5,pady=5,sticky=W)
        SNumber=Label(addmissionFrame,text="Mobile No:",font=("Arial",15,"bold"))
        SNumber.grid(row=11,column=0,padx=5,pady=5,sticky=W)
        SNumberEn=Entry(addmissionFrame,font=("Arial",15,"bold"),bd=3,width=25,textvariable=Snumber)
        SNumberEn.grid(row=11,column=1,padx=5,pady=5,sticky=W)

        SSubmit=Button(addmissionFrame,text="Submit Now!",font=("Arial",20,"bold"),bg="blue",fg="white",command=Ssubmit)
        SSubmit.grid(row=12,column=1,columnspan=2,padx=5,pady=5,sticky=W)

        AddmissionPanel.mainloop()

    def searchPanel():
        SearchPanel=Toplevel(userWindow)
        SearchPanel.title("Search Student")
        SearchPanel.geometry("400x150+300+10")
        def option_selected(event):
            if(SearchBo.get()!="Select"):
                SearchEntry.config(state=NORMAL)
                SearchBtn.config(state=NORMAL)

        # Searching Data and fetch to Display
        def searchData():
            try:
                conn=mysql.connector.connect(user="root",password="Mysql@123",host="localhost",port=3306,database="StudentManagement")
            except:
                messagebox.showwarning("Student Database","Database Not Found")
            else:
                cur=conn.cursor()
                # sql="SELECT *FROM STUDENT WHERE SRoll=%s or Registation_ID=%s or SNumber=%s or SEmail=%s or SName=%s"
                # cur.execute(sql,(Rollen.get(),Registration_Iden.get(),Mobile_noen.get(),Email_Iden.get(),Nameen.get()))
                if(SearchBo.get()=="Roll"):
                    sql="SELECT *FROM Student WHERE SRoll={}".format(SearchEntry.get())
                    cur.execute(sql)
                    fetchData=cur.fetchall()
                    if(len(fetchData)==0):
                        messagebox.showerror("Not Valid","Data not found",parent=SearchPanel)
                    else:
                        StudentTable.delete(*StudentTable.get_children())
                        for Data in fetchData:
                            StudentTable.insert("",END,values=Data)
                        conn.close()
                elif(SearchBo.get()=="Mobile_no"):
                    sql="SELECT *FROM Student WHERE SNumber={}".format(SearchEntry.get())
                    cur.execute(sql)
                    fetchData=cur.fetchall()
                    if(len(fetchData)==0):
                        messagebox.showerror("Not Valid","Data not found",parent=SearchPanel)
                    else:
                        StudentTable.delete(*StudentTable.get_children())
                        for Data in fetchData:
                            StudentTable.insert("",END,values=Data)
                        conn.close()
                elif(SearchBo.get()=="Email_Id"):
                    sql="SELECT *FROM Student WHERE SEmail={}".format(SearchEntry.get())
                    cur.execute(sql)
                    fetchData=cur.fetchall()
                    if(len(fetchData)==0):
                        messagebox.showerror("Not Valid","Data not found",parent=SearchPanel)
                    else:
                        StudentTable.delete(*StudentTable.get_children())
                        for Data in fetchData:
                            StudentTable.insert("",END,values=Data)
                        conn.close()
                elif(SearchBo.get()=="Name"):
                    sql="SELECT *FROM Student WHERE SName={}".format(SearchEntry.get())
                    cur.execute(sql)
                    fetchData=cur.fetchall()
                    if(len(fetchData)==0):
                        messagebox.showerror("Not Valid","Data not found",parent=SearchPanel)
                    else:
                        StudentTable.delete(*StudentTable.get_children())
                        for Data in fetchData:
                            StudentTable.insert("",END,values=Data)
                        conn.close()

        SearchBo=ttk.Combobox(SearchPanel,font=("Arial",15,"bold"),state="readonly",width=8,textvariable=SearchBox)
        SearchBo["value"]=("Select","Roll","Mobile_no","Email_Id","Name")
        SearchBo.current(0)
        SearchBo.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        SearchBo.bind("<<ComboboxSelected>>", option_selected)
        SearchEntry=Entry(SearchPanel,font=("Arial",15),bd=5,state=DISABLED)
        SearchEntry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        SearchBtn=Button(SearchPanel,text="Search",font=("Times new Roman",18,"bold"),bd=5,bg="yellow",fg="gray20",command=searchData)
        SearchBtn.grid(row=5,column=1,columnspan=2,pady=5)

        SearchPanel.mainloop()

    def showData():
        try:
            conn=mysql.connector.connect(user="root",password="Mysql@123",host="localhost",port=3306,database="StudentManagement")
        except:
            messagebox.showwarning("Student Database","Database Not Found")
        else:
            cur=conn.cursor()
            sql="SELECT *FROM STUDENT"
            cur.execute(sql)
            fetchData=cur.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for TableData in fetchData:
                Data=list(TableData)
                StudentTable.insert("",END,values=Data)

    def ConnectDB():
        AddmissionST.config(state=NORMAL)
        UpdationST.config(state=NORMAL)
        SearchST.config(state=NORMAL)
        Export.config(state=NORMAL)
        DeleteST.config(state=NORMAL)
        ShowST.config(state=NORMAL)

    def ExitAdmin():
        op=messagebox.askyesno("Close Window","Are you sure to Exit")
        if (op>0):
            messagebox.showinfo("Bye!","Thank You for Visit")
            root.destroy()
        else:
            messagebox.showinfo("Close","Your current Window Close ")
            userWindow.destroy()

    # Background Image
    Background=ImageTk.PhotoImage(file="project\\StudentManagement\\b1.jpg")
    bg=Label(userWindow,image=Background)
    bg.place(x=0,y=0)
    HeadingIm=ImageTk.PhotoImage(file="project\\StudentManagement\\bg1.jpg")
    Heading=Label(userWindow,image=HeadingIm,font=("Times New Roman",30,"bold"),width=800,height=80)
    Heading.pack(fill=X)
    HeadingT=Label(userWindow,text="Tarkeshwar Prasad Varma College ",font=("Times New Roman",30,"bold"),fg="gold",bg="blue")
    HeadingT.place(x=360,y=4)


    DBC=Button(userWindow,text="Connect DataBase",font=("Arial",15,"bold"),bd=5,bg="gray20",fg="white",activebackground="Yellow",command=ConnectDB)
    DBC.place(x=1120,y=25)

    Option=Frame(userWindow,bd=5,bg="gold")
    Option.place(x=30,y=100)

    AddmissionST=Button(Option,text="Addmission",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,state=DISABLED,cursor="hand2",command=addmissionPanel)
    AddmissionST.grid(row=0,column=0,padx=20,pady=20,sticky=W)
    UpdationST=Button(Option,text="Update",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,state=DISABLED,cursor="hand2",command=updatePanel)
    UpdationST.grid(row=1,column=0,padx=20,pady=20,sticky=W)
    SearchST=Button(Option,text="Search",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,state=DISABLED,cursor="hand2",command=searchPanel)
    SearchST.grid(row=2,column=0,padx=20,pady=20,sticky=W)
    ShowST=Button(Option,text="Show Data",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,state=DISABLED,cursor="hand2",command=showData)
    ShowST.grid(row=3,column=0,padx=20,pady=20,sticky=W)
    DeleteST=Button(Option,text="Delete",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,state=DISABLED,cursor="hand2",command=deleteData)
    DeleteST.grid(row=4,column=0,padx=20,pady=20,sticky=W)
    Exit=Button(Option,text="Exit",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,cursor="hand2",command=ExitAdmin)
    Exit.grid(row=5,column=0,padx=20,pady=20,sticky=W)
    Export=Button(Option,text="Export",font=("Arial",15,"bold"),bg="blue",fg="white",bd=5,width=18,state=DISABLED,cursor="hand2",command=exportData)
    Export.grid(row=6,column=0,padx=20,pady=20,sticky=W)

    # Display Frame
    OutputFrame=Frame(userWindow,bd=5,bg="gold")
    OutputFrame.place(x=300,y=100,width=1000,height=630)

    OutputScrollX=Scrollbar(OutputFrame,orient=VERTICAL)
    OutputScrollX.pack(side=RIGHT,fill=Y)
    OutputScrollY=Scrollbar(OutputFrame,orient=HORIZONTAL)
    OutputScrollY.pack(side=BOTTOM,fill=X)

    StudentTable=ttk.Treeview(OutputFrame,yscrollcommand=OutputScrollX.set,xscrollcommand=OutputScrollY.set)
    StudentTable["columns"]=("Reg","Name","Rol","Sub","Gmail","Dob","State","Dist","Gender","Cast","Nation","Num")
    style=ttk.Style()
    style.configure("Treeview",font=("Arial",10),rowheight=30)
    style.configure("Treeview.Heading",font=("Arial",12))

    # Table width
    StudentTable.column("Reg",width=120,anchor=CENTER)
    StudentTable.column("Name",width=180,anchor=CENTER)
    StudentTable.column("Rol",width=100,anchor=CENTER)
    StudentTable.column("Sub",width=180,anchor=CENTER)
    StudentTable.column("Gmail",width=180,anchor=CENTER)
    StudentTable.column("Dob",width=120,anchor=CENTER)
    StudentTable.column("State",width=150,anchor=CENTER)
    StudentTable.column("Dist",width=180,anchor=CENTER)
    StudentTable.column("Gender",width=80,anchor=CENTER)
    StudentTable.column("Cast",width=80,anchor=CENTER)
    StudentTable.column("Nation",width=180,anchor=CENTER)
    StudentTable.column("Num",width=100,anchor=CENTER)
    # Table Heading
    StudentTable.heading("Reg",text="Registration_ID")
    StudentTable.heading("Name",text="Name")
    StudentTable.heading("Rol",text="Roll")
    StudentTable.heading("Sub",text="Subject")
    StudentTable.heading("Gmail",text="Email_Id")
    StudentTable.heading("Dob",text="Date of Birth")
    StudentTable.heading("State",text="State")
    StudentTable.heading("Dist",text="District")
    StudentTable.heading("Gender",text="Gender")
    StudentTable.heading("Cast",text="Caste")
    StudentTable.heading("Nation",text="Nationality")
    StudentTable.heading("Num",text="Mobile_No")

    StudentTable.pack(fill=BOTH,expand=1)
    StudentTable["show"]="headings" #It removes unnecessary column which comes on 0th index
    OutputScrollX.config(command=StudentTable.yview)
    OutputScrollY.config(command=StudentTable.xview)

    userWindow.mainloop()
# Login Function
def AdminLogin():
    if(usernameEn.get()=="" or passwordEn.get()==""):
        messagebox.showwarning("Warning","Username or Password can't Empty")
    else:
        try:
            conn=mysql.connector.connect(
                user="root",
                password="Mysql@123",
                host="localhost",
                port=3306,
                database="studentmanagement")
        except:
            messagebox.showerror("Database not Connected")
        else:
            cur=conn.cursor()
            sql="SELECT *FROM registration"
            cur.execute(sql)
            lst=cur.fetchall()
            for i in range(0,len(lst)):
                for j in range(0,6):
                    if(UsernameN.get()==lst[i][j]):
                        for k in range(0,len(lst)):
                            for l in range(0,6):
                                if(PasswordN.get()==lst[k][l]):
                                    messagebox.showinfo("Successful","Congrats Welcome to TPVC")
                                    UserWindow()
                                    # print(lst[i][j])
                                    # print(lst[k][l])

def AdminRegister():
    register=Toplevel(root)
    register.title("Registration")
    register.geometry("400x380+100+20")
    register.resizable(0,0)

    def AdminSubmit():
        if(Name.get()=="" or Email.get()=="" or Phone.get()=="" or Username.get()=="" or Password.get()==""):
            messagebox.showwarning("Empty","All fields are mendatory")
            register.destroy()
        else:
            if("@gmail.com" in Email.get() and len(Phone.get())==10):
                try:
                    conn=mysql.connector.connect(
                        user="root",
                        password="Mysql@123",
                        host="localhost",
                        port=3306,
                        database="studentmanagement")
                except:
                    messagebox.showerror("Database not Connected")
                else:
                    cur=conn.cursor()
                    cur.execute("insert into registration values(%s,%s,%s,%s,%s,%s)",(Name.get(),Email.get(),Gender.get(),Phone.get(),Username.get(),Password.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Successful","Data Inserted")
                finally:
                    Name.set("")
                    Email.set("")
                    Gender.set("")
                    Phone.set("")
                    Username.set("")
                    Password.set("")
            else:
                messagebox.showerror("Fields are not proper","Email_Id or Phone_No not Proper",parent=register)
        
    registerFrame=LabelFrame(register,text="User Registration",font=("Arial",15,"bold"))
    registerFrame.place(x=50,y=10)

    NameLabel=Label(registerFrame,text="Name",font=("Arial",12,"bold"))
    NameLabel.grid(row=0,column=0,sticky=W)
    NameEn=Entry(registerFrame,font=("Arial",12,"bold"),textvariable=Name)
    NameEn.grid(row=0,column=1,padx=10,pady=10)

    EmailLabel=Label(registerFrame,text="Email",font=("Arial",12,"bold"))
    EmailLabel.grid(row=1,column=0,sticky=W)
    EmailEn=Entry(registerFrame,font=("Arial",12,"bold"),textvariable=Email)
    EmailEn.grid(row=1,column=1,padx=10,pady=10)

    GenderLabel=Label(registerFrame,text="Gender",font=("Arial",12,"bold"))
    GenderLabel.grid(row=2,column=0,sticky=W)    
    GenderBox=ttk.Combobox(registerFrame,text="Gender",font=("Arial",12,"bold"),state="readonly",width=8,textvariable=Gender)
    GenderBox["value"]=("Male","Female","Transgender")
    GenderBox.current(0)
    GenderBox.grid(row=2,column=1,padx=10,pady=10,sticky=W)

    PhoneLabel=Label(registerFrame,text="Phone No",font=("Arial",12,"bold"))
    PhoneLabel.grid(row=3,column=0,sticky=W)
    PhoneEn=Entry(registerFrame,font=("Arial",12,"bold"),textvariable=Phone)
    PhoneEn.grid(row=3,column=1,padx=10,pady=10)

    UserLabel=Label(registerFrame,text="User Name",font=("Arial",12,"bold"))
    UserLabel.grid(row=4,column=0,sticky=W)
    UserEn=Entry(registerFrame,font=("Arial",12,"bold"),textvariable=Username)
    UserEn.grid(row=4,column=1,padx=10,pady=10)

    PasswordLabel=Label(registerFrame,text="Password",font=("Arial",12,"bold"))
    PasswordLabel.grid(row=5,column=0,sticky=W)
    PasswordEn=Entry(registerFrame,font=("Arial",12,"bold"),textvariable=Password)
    PasswordEn.grid(row=5,column=1,padx=10,pady=10)

    SubmitBtn=Button(registerFrame,text="Submit",font=("Arial",15,"bold"),bg="blue",fg="white",activebackground="yellow",cursor="hand2",command=AdminSubmit)
    SubmitBtn.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
    register.mainloop()

# Background Image
Background=ImageTk.PhotoImage(file="project\\StudentManagement\\bg1.jpg")
bg=Label(root,image=Background)
bg.place(x=0,y=0)

loginFrame=Frame(root,bg="gray50")
loginFrame.place(x=550,y=150)

logoImage=PhotoImage(file="project\\StudentManagement\\logo.png")
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

usernameImage=PhotoImage(file="project\\StudentManagement\\user.png")
usernameLabel=Label(loginFrame,text="Username",font=("Arial",12,"bold"),image=usernameImage,compound=LEFT,bg="gray50")
usernameLabel.grid(row=1,column=0,padx=10,pady=10)
usernameEn=Entry(loginFrame,font=("Arial",15,"bold"),width=15,bd=5,textvariable=UsernameN)
usernameEn.grid(row=1,column=1,padx=10,pady=10)

passwordImage=PhotoImage(file="project\StudentManagement\password.png")
passwordLabel=Label(loginFrame,text="Password",font=("Arial",12,"bold"),image=passwordImage,compound=LEFT,bg="gray50")
passwordLabel.grid(row=2,column=0,padx=10,pady=10)
passwordEn=Entry(loginFrame,font=("Arial",15,"bold"),width=15,bd=5,textvariable=PasswordN)
passwordEn.grid(row=2,column=1,padx=10,pady=10)

LoginButton=Button(loginFrame,font=("Arial",15,"bold"),text="Login",bd=5,activebackground="blue",activeforeground="white",width=8,cursor="hand2",command=AdminLogin)
LoginButton.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

RegisterButton=Button(root,font=("Arial",15,"bold"),text="Register",width=10,cursor="hand2",activebackground="blue",activeforeground="white",command=AdminRegister)
RegisterButton.place(x=1220,y=10)

root.mainloop()
