from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x760+0+0")
        self.root.title("Student Management System")

        # Variables
        self.dept=StringVar()
        self.course=StringVar()
        self.year=StringVar()
        self.sem=StringVar()
        self.stdId=StringVar()
        self.stdName=StringVar()
        self.stdEmail=StringVar()
        self.stdRoll=StringVar()
        self.stdMob=StringVar()
        self.stdAdd=StringVar()
        self.stdGender=StringVar()
        self.stdDob=StringVar()


        img1=Image.open(r"project\StudentManagementSystem\Images\7th.jpg")
        self.Bg1=ImageTk.PhotoImage(img1)
        self.bt1=Button(root,image=self.Bg1)
        self.bt1.place(x=0,y=0,width=455,height=160)
        img2=Image.open(r"project\StudentManagementSystem\Images\8th.jpg")
        self.Bg2=ImageTk.PhotoImage(img2)
        self.bt2=Button(root,image=self.Bg2)
        self.bt2.place(x=455,y=0,width=455,height=160)
        img3=Image.open(r"project\StudentManagementSystem\Images\9th.jpg")
        self.Bg3=ImageTk.PhotoImage(img3)
        self.bt3=Button(root,image=self.Bg3)
        self.bt3.place(x=910,y=0,width=455,height=160)

        # College Name
        self.lbl_title=Label(self.root,text="TARKESHWAR PRASAD VARMA COLLEGE,NARKATIYAGANJ",font=("Algerian",25),fg="blue")
        self.lbl_title.place(x=0,y=160,width=1366,height=60)

        # Main Frame
        self.frame=Frame(self.root,bg="yellow")
        self.frame.place(x=0,y=220,width=1360,height=548)

        # Left Frame
        self.LFrame=LabelFrame(self.root,text="Student Information",relief=RIDGE,bd=5,font=("Times New Roman",12,"bold"),bg="cyan")
        self.LFrame.place(x=2,y=224,width=683,height=470)

        # Current Courses
        currentCourse=LabelFrame(self.LFrame,text="Current Courses",font=("Arial",10,"bold"),fg="green")
        currentCourse.place(x=5,y=5,width=665,height=120)

        # Department
        Dept=Label(currentCourse,text="Department",font=("Arial",10,"bold"))
        Dept.grid(row=0,column=0,padx=10,pady=15)

        DeptBox=ttk.Combobox(currentCourse,state="readonly",font=("Arial",10,"bold"),textvariable=self.dept)
        DeptBox["value"]=("Select Department","Computer Science","Arts","Science","Management","LLB")
        DeptBox.current(0)
        DeptBox.grid(row=0,column=1,sticky=W)

        # Courses
        Course=Label(currentCourse,text="Courses",font=("Arial",10,"bold"))
        Course.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        CourseBox=ttk.Combobox(currentCourse,state="readonly",font=("Arial",10,"bold"),textvariable=self.course)
        CourseBox["value"]=("Select Courses","BCA","BBA","Bio-tech","BA","BSC")
        CourseBox.current(0)
        CourseBox.grid(row=0,column=3,sticky=W)

        # Year
        Year=Label(currentCourse,text="Year",font=("Arial",10,"bold"))
        Year.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        YearBox=ttk.Combobox(currentCourse,state="readonly",font=("Arial",10,"bold"),textvariable=self.year)
        YearBox["value"]=("Select Year","2017-20","2020-23","2023-26","2026-29","2029-32")
        YearBox.current(0)
        YearBox.grid(row=1,column=1,sticky=W)

        # Semester
        Sem=Label(currentCourse,text="Semester",font=("Arial",10,"bold"))
        Sem.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        SemBox=ttk.Combobox(currentCourse,state="readonly",font=("Arial",10,"bold"),textvariable=self.sem)
        SemBox["value"]=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        SemBox.current(0)
        SemBox.grid(row=1,column=3,sticky=W)

        # Student Class Information
        Student_Class_Info=LabelFrame(self.LFrame,text="Student Class Information",font=("Arial",10,"bold"),fg="green")
        Student_Class_Info.place(x=5,y=130,width=665,height=310)

        StudId=Label(Student_Class_Info,text="Student ID",font=("Arial",10,"bold"))
        StudId.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        StudIdEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdId)
        StudIdEn.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        StudName=Label(Student_Class_Info,text="Name",font=("Arial",10,"bold"))
        StudName.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        StudNameEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdName)
        StudNameEn.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        StudRoll=Label(Student_Class_Info,text="Roll No",font=("Arial",10,"bold"))
        StudRoll.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        StudRollEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdRoll)
        StudRollEn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        StudPhone=Label(Student_Class_Info,text="Mobile No",font=("Arial",10,"bold"))
        StudPhone.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        StudPhoneEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdMob)
        StudPhoneEn.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        StudEmail=Label(Student_Class_Info,text="Email",font=("Arial",10,"bold"))
        StudEmail.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        StudEmailEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdEmail)
        StudEmailEn.grid(row=2,column=1,padx=5,pady=5,sticky=W)  

        StudAddress=Label(Student_Class_Info,text="Address",font=("Arial",10,"bold"))
        StudAddress.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        StudAddressEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdAdd)
        StudAddressEn.grid(row=2,column=3,padx=5,pady=5,sticky=W)  

        Gender=Label(Student_Class_Info,text="Gender",font=("Arial",10,"bold"))
        Gender.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        GenderBox=ttk.Combobox(Student_Class_Info,state="readonly",font=("Arial",10,"bold"),width=10,textvariable=self.stdGender)
        GenderBox["value"]=("Male","Female")
        GenderBox.current(0)
        GenderBox.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        StudDOB=Label(Student_Class_Info,text="Date of Birth",font=("Arial",10,"bold"))
        StudDOB.grid(row=3,column=2,padx=5,pady=5,sticky=W)
        StudDOBEn=Entry(Student_Class_Info,font=("Arial",10,"bold"),width=30,textvariable=self.stdDob)
        StudDOBEn.grid(row=3,column=3,padx=5,pady=15,sticky=W)      

        # Button
        Reset=Button(Student_Class_Info,text="Reset",font=("Arial",15,"bold"),width=15,bg="blue",fg="white",command=self.reset)
        Reset.grid(row=4,column=1,padx=5,pady=15,sticky=W) 
        Update=Button(Student_Class_Info,text="Update",font=("Arial",15,"bold"),width=15,bg="blue",fg="white",command=self.update)
        Update.grid(row=4,column=3,padx=5,pady=15,sticky=W)
        Delete=Button(Student_Class_Info,text="Delete",font=("Arial",15,"bold"),width=15,bg="blue",fg="white",command=self.delete)
        Delete.grid(row=5,column=1,padx=5,pady=15,sticky=W)
        Save=Button(Student_Class_Info,text="Save",font=("Arial",15,"bold"),width=15,bg="blue",fg="white",command=self.add_data)
        Save.grid(row=5,column=3,padx=5,pady=15,sticky=W)

        # Right Frame
        self.RFrame=LabelFrame(self.root,text="Student Details",relief=RIDGE,bd=5,font=("Times New Roman",12,"bold"),bg="cyan")
        self.RFrame.place(x=685,y=224,width=670,height=470)

        # Image
        img4=Image.open(r"project\StudentManagementSystem\Images\university.jpg")
        self.Bg4=ImageTk.PhotoImage(img4)
        self.bt4=Button(self.RFrame,image=self.Bg4)
        self.bt4.place(x=2,y=2,width=658,height=170)
        # Search Student Information Frame
        Search_Student_Info=LabelFrame(self.RFrame,text="Search Student Information")
        Search_Student_Info.place(x=2,y=175,width=658,height=50)

        # Search label
        SearchBy=Label(Search_Student_Info,text="Search By",font=("Arial",12,"bold"),width=10)
        SearchBy.grid(row=0,column=0,padx=0,sticky=W)

        # Search Combobox
        self.searchBy=StringVar()
        SearchBy=ttk.Combobox(Search_Student_Info,state="readonly",font=("Arial",10,"bold"),width=10,textvariable=self.searchBy)
        SearchBy["value"]=("Select","Roll","Name")
        SearchBy.current(0)
        SearchBy.grid(row=0,column=1,padx=0,sticky=W)

        # Search Entry
        self.search=StringVar()
        SearchEn=Entry(Search_Student_Info,font=("Arial",12),width=25,textvariable=self.search)
        SearchEn.grid(row=0,column=2,padx=5,sticky=W)

        # Search button
        SearchButton=Button(Search_Student_Info,text="Search",font=("Arial",10),bg="blue",fg="white",command=self.Search)
        SearchButton.grid(row=0,column=3,padx=5,sticky=W)

        # Show All Button
        ShowAllButton=Button(Search_Student_Info,text="Show All ",font=("Arial",10),bg="blue",fg="white",command=self.fetch)
        ShowAllButton.grid(row=0,column=4,padx=5,sticky=W)

        # Show Information
        ShowInfoTable=LabelFrame(self.RFrame)
        ShowInfoTable.place(x=2,y=225,width=658,height=220)

        scroll_x=ttk.Scrollbar(ShowInfoTable,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(ShowInfoTable,orient=VERTICAL)
        self.Student_Table=ttk.Treeview(ShowInfoTable,column=("Department","Courses","year","Semester","Student_ID","Name","Roll","Mobile_No","Email","Address","Gender","DOB"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)

        self.Student_Table.heading("Department",text="Department")
        self.Student_Table.heading("Courses",text="Courses")
        self.Student_Table.heading("year",text="Year")
        self.Student_Table.heading("Semester",text="Semester")
        self.Student_Table.heading("Student_ID",text="Student_ID")
        self.Student_Table.heading("Name",text="Name")
        self.Student_Table.heading("Roll",text="Roll")
        self.Student_Table.heading("Mobile_No",text="Mobile_No")
        self.Student_Table.heading("Email",text="Email")
        self.Student_Table.heading("Address",text="Address")
        self.Student_Table.heading("Gender",text="Gender")
        self.Student_Table.heading("DOB",text="DOB")

        self.Student_Table.column("Department",width=130)
        self.Student_Table.column("Courses",width=100)
        self.Student_Table.column("year",width=100)
        self.Student_Table.column("Semester",width=100)
        self.Student_Table.column("Student_ID",width=100)
        self.Student_Table.column("Name",width=140)
        self.Student_Table.column("Roll",width=100)
        self.Student_Table.column("Mobile_No",width=100)
        self.Student_Table.column("Email",width=180)
        self.Student_Table.column("Address",width=200)
        self.Student_Table.column("Gender",width=80)
        self.Student_Table.column("DOB",width=80)

        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table["show"]="headings"
        self.Student_Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch()


    def add_data(self):
        if(self.stdName.get()!="" and self.stdId.get()!=""and self.stdMob.get()!=""and self.stdRoll.get()!="" and self.stdEmail.get()!="" and self.stdAdd.get()!="" and self.stdGender.get()!="" and self.stdDob.get()!="" and self.dept.get()!="" and self.course.get()!="" and self.year.get()!="" and self.sem.get()!="" ):
            try:
                conn=mysql.connector.connect(
                    user='root',
                    password='Mysql@123',
                    host='localhost',
                    port=3306,
                    database="StudentManagementSystem"
                )
            except Exception as obj:
                messagebox.showerror("Database not connected")
            else:
                cursor=conn.cursor()
                cursor.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.dept.get(),self.course.get(),self.year.get(),self.sem.get(),
                    self.stdId.get(),self.stdName.get(),self.stdRoll.get(),self.stdMob.get(),
                    self.stdEmail.get(),self.stdAdd.get(),self.stdGender.get(),self.stdDob.get()))
                conn.commit()
                self.fetch()
                messagebox.showinfo("Success","Data inserted Successful")
                conn.close()
        else:
            messagebox.showerror("Blank","All fields are mendatory")

    def reset(self):
        self.dept.set("Select Department")
        self.course.set("Select Courses")
        self.year.set("Select Year")
        self.sem.set("Select Semester")
        self.stdId.set("")
        self.stdName.set("")
        self.stdRoll.set("")
        self.stdMob.set("")
        self.stdEmail.set("")
        self.stdAdd.set("")
        self.stdGender.set("Male")
        self.stdDob.set("")

    def fetch(self):
        try:
            conn=mysql.connector.connect(
                user='root',
                password='Mysql@123',
                host='localhost',
                port=3306,
                database="StudentManagementSystem"
                )
        except:
            messagebox.showerror("Database not connected")
        else:
            mycur=conn.cursor()
            mycur.execute("SELECT *FROM Student")#Ise use karne ke bad sabhi data mycur me aa jata hai 
            data=mycur.fetchall() #fetchall method lagake sabhi data ko data variable me rakha gya hai
            if (len(data)!=0):
                self.Student_Table.delete(*self.Student_Table.get_children())
                for i in data:
                    self.Student_Table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def update(self):
        if(self.stdName.get()==""):
            messagebox.showerror("Blank","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update")
                if(update>0):
                    conn=mysql.connector.connect(
                        user='root',
                        password='Mysql@123',
                        host='localhost',
                        port=3306,
                        database="StudentManagementSystem"
                    )
                    mycur=conn.cursor()
                    mycur.execute("UPDATE Student SET Department='{}',Courses='{}',year='{}',Semester='{}',Name='{}',Roll='{}',Mobile_No='{}',Email='{}',Address='{}',Gender='{}',DOB='{}' WHERE Student_ID='{}'".format(self.dept.get(),self.course.get(),self.year.get(),self.sem.get(),
                        self.stdName.get(),self.stdRoll.get(),self.stdMob.get(),
                        self.stdEmail.get(),self.stdAdd.get(),self.stdGender.get(),
                        self.stdDob.get(),self.stdId.get()))
                    # sql="update Student set Department='{}',Courses='{}',year='{}',Semester='{}',Name='{}',Roll='{}',Mobile_No='{}',Email='{}',Address='{}',Gender='{}',DOB='{}'WHERE Student_ID='{}'".format(self.dept.get(),self.course.get(),self.year.get(),self.sem.get(),self.stdName.get(),self.stdRoll.get(),self.stdMob.get(),self.stdEmail.get(),self.stdAdd.get(),self.stdGender.get(),self.stdDob.get(),self.stdId.get())
                    # sql="update Student set Department='{}',Courses='{}',year='{}',Semester='{}',Name='{}',Roll='{}',Mobile_No='{}',Email='{}',Address='{}',Gender='{}',DOB='{}' WHERE Student_ID='{}'".format(self.dept.get(),self.course.get(),self.year.get(),self.sem.get(),self.stdName.get(),self.stdRoll.get(),self.stdMob.get(),self.stdEmail.get(),self.stdAdd.get(),self.stdGender.get(),self.stdDob.get(),self.stdId.get())
                    # mycur.execute(sql)
                else:
                    return
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo("Success"," Data Updated")
            except:
                messagebox.showerror("Warning","Data not updated")

    def delete(self):
        if(self.stdName.get()==""):
            messagebox.showerror("Blank","All fields are required")
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure")
                if(delete>0):
                    conn=mysql.connector.connect(
                        user='root',
                        password='Mysql@123',
                        host='localhost',
                        port=3306,
                        database="StudentManagementSystem"
                    )
                    mycur=conn.cursor()
                    mycur.execute("DELETE FROM Student WHERE Student_ID='{}'".format(self.stdId.get()))
                    conn.commit()
                    self.fetch()
                    conn.close()
                    messagebox.showinfo("Delete","Data will deleted")
                else:
                    return
            except:
                messagebox.showerror("Warning","Data not deleted")
                
    def Search(self):
        if(self.search.get()==""):
            messagebox.showerror("Search","Please type on Search Bar")
        else:
            try:
                conn=mysql.connector.connect(
                    user='root',
                    password='Mysql@123',
                    host='localhost',
                    port=3306,
                    database="StudentManagementSystem"
                    )
                mycur=conn.cursor()
                sql="SELECT *FROM Student WHERE "+str(self.searchBy.get())+" LIKE '%"+str(self.search.get())+"%'"
                mycur.execute(sql)
                data=mycur.fetchall()
                if len(data)!=0:
                    self.Student_Table.delete(*self.Student_Table.get_children())
                    for i in data:
                        self.Student_Table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except:
                messagebox.showerror("Warning","Data not found")

    def get_cursor(self,event=""):
        cursor=self.Student_Table.focus()
        content=self.Student_Table.item(cursor)
        data=content["values"]

        self.dept.set(data[0])
        self.course.set(data[1])
        self.year.set(data[2])
        self.sem.set(data[3])
        self.stdId.set(data[4])
        self.stdName.set(data[5])
        self.stdRoll.set(data[6])
        self.stdMob.set(data[7])
        self.stdEmail.set(data[8])
        self.stdAdd.set(data[9])
        self.stdGender.set(data[10])
        self.stdDob.set(data[11])

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()