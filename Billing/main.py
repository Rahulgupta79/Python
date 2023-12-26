from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("1360x740")
# root.resizable(0,0)
root.configure(bg="gray20")
heading=Label(root,text="Retail Billing System",font=("Times new Roman",35),relief=GROOVE,bg="gray20",fg="gold",bd=8)
heading.pack(fill=X)


CosmeticPriceV=IntVar()
GroceryPriceV=IntVar()
ColdDrinkPriceV=IntVar()
# Variables
soap=IntVar()
facecream=IntVar()
facewash=IntVar()
hairspray=IntVar()
hairgel=IntVar()
bodylotion=IntVar()
rice=IntVar()
oil=IntVar()
dal=IntVar()
wheat=IntVar()
sugar=IntVar()
tea=IntVar()
mazza=IntVar()
pepsi=IntVar()
sprite=IntVar()
dew=IntVar()
frooti=IntVar()
cocacola=IntVar()
# Price List
P_soap=10
P_facecream=100
P_facewash=150
P_hairspray=220
P_hairgel=60
P_bodylotion=250
P_rice=40
P_oil=90
P_dal=80
P_wheat=60
P_sugar=40
P_tea=60
P_mazza=100
P_pepsi=100
P_sprite=100
P_dew=100
P_frooti=100
P_cocacola=100

# Function
def totalPrice():
    S=soap.get()*P_soap
    FC=facecream.get()*P_facecream
    FW=facewash.get()*P_facewash
    HS=hairspray.get()*220
    HG=hairgel.get()*60
    BL=bodylotion.get()*250
    totalCosmeticP=S+FC+FW+HS+HG+BL
    CosmeticPriceV.set(totalCosmeticP)

    R=rice.get()*P_rice
    O=oil.get()*P_oil
    Da=dal.get()*P_dal
    W=wheat.get()*P_wheat
    Su=sugar.get()*P_sugar
    T=tea.get()*P_tea
    totalGroceryP=R+O+Da+W+Su+T
    GroceryPriceV.set(totalGroceryP)

    M=mazza.get()*P_mazza
    P=pepsi.get()*P_pepsi
    Sp=sprite.get()*P_sprite
    De=dew.get()*P_dew
    F=frooti.get()*P_frooti
    C=cocacola.get()*P_cocacola
    totalColdP=M+P+Sp+De+F+C
    ColdDrinkPriceV.set(totalColdP)

def Clear():
    CosmeticPriceV.set(0)
    GroceryPriceV.set(0)
    ColdDrinkPriceV.set(0)
    soap.set(0)
    facecream.set(0)
    facewash.set(0)
    hairspray.set(0)
    hairgel.set(0)
    bodylotion.set(0)
    rice.set(0)
    oil.set(0)
    dal.set(0)
    wheat.set(0)
    sugar.set(0)
    tea.set(0)
    mazza.set(0)
    pepsi.set(0)
    sprite.set(0)
    dew.set(0)
    frooti.set(0)
    cocacola.set(0)


# def BillBox():
#         SemBox=ttk.Combobox(currentCourse,state="readonly",font=("Arial",10,"bold"),textvariable=self.sem)
#         SemBox["value"]=("Select Semester","1st","2nd","3rd","4th","5th","6th")
#         SemBox.current(0)
#         SemBox.grid(row=1,column=3,sticky=W)
#         pass



# Customer Details
customer_frame=LabelFrame(root,bg="gray20",fg="gold",text="Customer Details",font=("Arial",15),bd=5)
customer_frame.pack(fill=X)

Name=Label(customer_frame,text="Name",bg="gray20",fg="white",font=("Arial",15),height=2)
Name.grid(row=0,column=0)
NameEntry=Entry(customer_frame,font=("arial",12,"bold"),width=18,bd=5)
NameEntry.grid(row=0,column=1,padx=30,pady=10)

Phone_No=Label(customer_frame,text="Phone Number",bg="gray20",fg="white",font=("arial",15,"bold"),height=2)
Phone_No.grid(row=0,column=2)
Phone_NoEntry=Entry(customer_frame,font=("arial",12,"bold"),width=18,bd=5)
Phone_NoEntry.grid(row=0,column=3,padx=30,pady=10)

Bill=Label(customer_frame,text="Bill Number",bg="gray20",fg="white",font=("arial",15,"bold"),height=2)
Bill.grid(row=0,column=4)
BillEntry=Entry(customer_frame,font=("arial",12,"bold"),width=18,bd=5)
BillEntry.grid(row=0,column=5,padx=40,pady=10)

SearchEntry=Button(customer_frame,text="Search",font=("arial",12,"bold"),width=10,bd=5)
SearchEntry.grid(row=0,column=7,pady=10)

# Products
productFrame=Frame(root,bg="gray20")
productFrame.pack(fill=X)

cosmeticFrame=LabelFrame(productFrame,text="Cosmetics",bg="gray20",fg="gold",font=("Arial",15),width=25)
cosmeticFrame.grid(row=0,column=0,padx=5)
bathSoap=Label(cosmeticFrame,text="Bath Soap",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
bathSoap.grid(row=0,column=0,sticky=W,padx=5)
bathSoapEn=Entry(cosmeticFrame,text="Bath Soap",width=10,bd=5,textvariable=soap,font=("arial",12,"bold"))
bathSoapEn.grid(row=0,column=1,pady=10)



# bathSoapEn=ttk.Combobox(cosmeticFrame,state="readonly",font=("Arial",10,"bold"))


faceCream=Label(cosmeticFrame,text="Face Cream",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
faceCream.grid(row=1,column=0,sticky=W,padx=5)
faceCreamEn=Entry(cosmeticFrame,text="Face Cream",width=10,bd=5,textvariable=facecream,font=("arial",12,"bold"))
faceCreamEn.grid(row=1,column=1,pady=10)
faceWash=Label(cosmeticFrame,text="Face Wash",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
faceWash.grid(row=2,column=0,sticky=W,padx=5)
faceWashEn=Entry(cosmeticFrame,text="Face Wash",width=10,bd=5,textvariable=facewash,font=("arial",12,"bold"))
faceWashEn.grid(row=2,column=1,pady=10)
hairSpray=Label(cosmeticFrame,text="Hair Spray",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
hairSpray.grid(row=3,column=0,sticky=W,padx=5)
hairSprayEn=Entry(cosmeticFrame,text="Hair Spray",width=10,bd=5,textvariable=hairspray,font=("arial",12,"bold"))
hairSprayEn.grid(row=3,column=1,pady=10)
hairGel=Label(cosmeticFrame,text="Hair Gel",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
hairGel.grid(row=4,column=0,sticky=W,padx=5)
hairGelEn=Entry(cosmeticFrame,text="Hair Gel",width=10,bd=5,textvariable=hairgel,font=("arial",12,"bold"))
hairGelEn.grid(row=4,column=1,pady=10)
bodyLotion=Label(cosmeticFrame,text="Body Lotion",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
bodyLotion.grid(row=5,column=0,sticky=W,padx=5)
bodyLotionEn=Entry(cosmeticFrame,text="Body Lotion",width=10,bd=5,textvariable=bodylotion,font=("arial",12,"bold"))
bodyLotionEn.grid(row=5,column=1,pady=20)

groceryFrame=LabelFrame(productFrame,text="Grocery",bg="gray20",fg="gold",font=("Arial",15),width=25)
groceryFrame.grid(row=0,column=1,padx=5)
Rice=Label(groceryFrame,text="Rice",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Rice.grid(row=0,column=0,sticky=W,padx=5)
RiceEn=Entry(groceryFrame,text="Rice",width=10,bd=5,textvariable=rice,font=("arial",12,"bold"))
RiceEn.grid(row=0,column=1,pady=10)
Oil=Label(groceryFrame,text="Oil",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Oil.grid(row=1,column=0,sticky=W,padx=5)
OilEn=Entry(groceryFrame,text="Oil",width=10,bd=5,textvariable=oil,font=("arial",12,"bold"))
OilEn.grid(row=1,column=1,pady=10)
Dal=Label(groceryFrame,text="Dal",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Dal.grid(row=2,column=0,sticky=W,padx=5)
DalEn=Entry(groceryFrame,text="Dal",width=10,bd=5,textvariable=dal,font=("arial",12,"bold"))
DalEn.grid(row=2,column=1,pady=10)
Wheat=Label(groceryFrame,text="Wheat",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Wheat.grid(row=3,column=0,sticky=W,padx=5)
WheatEn=Entry(groceryFrame,text="Wheat",width=10,bd=5,textvariable=wheat,font=("arial",12,"bold"))
WheatEn.grid(row=3,column=1,pady=10)
Sugar=Label(groceryFrame,text="Sugar",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Sugar.grid(row=4,column=0,sticky=W,padx=5)
SugarEn=Entry(groceryFrame,text="Sugar",width=10,bd=5,textvariable=sugar,font=("arial",12,"bold"))
SugarEn.grid(row=4,column=1,pady=10)
Tea=Label(groceryFrame,text="Tea",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Tea.grid(row=5,column=0,sticky=W,padx=5)
TeaEn=Entry(groceryFrame,text="Tea",width=10,bd=5,textvariable=tea,font=("arial",12,"bold"))
TeaEn.grid(row=5,column=1,pady=20)

coldDrinksFrame=LabelFrame(productFrame,text="Cold Drinks",bg="gray20",fg="gold",font=("Arial",15))
coldDrinksFrame.grid(row=0,column=2,padx=10)
Mazza=Label(coldDrinksFrame,text="Mazza",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Mazza.grid(row=0,column=0,sticky=W,padx=5)
MazzaEn=Entry(coldDrinksFrame,text="Mazza",width=10,bd=5,textvariable=mazza,font=("arial",12,"bold"))
MazzaEn.grid(row=0,column=1,pady=10)
Pepsi=Label(coldDrinksFrame,text="Pepsi",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Pepsi.grid(row=1,column=0,sticky=W,padx=5)
PepsiEn=Entry(coldDrinksFrame,text="Pepsi",width=10,bd=5,textvariable=pepsi,font=("arial",12,"bold"))
PepsiEn.grid(row=1,column=1,pady=10)
Sprite=Label(coldDrinksFrame,text="Sprite",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Sprite.grid(row=2,column=0,sticky=W,padx=5)
SpriteEn=Entry(coldDrinksFrame,text="Sprite",width=10,bd=5,textvariable=sprite,font=("arial",12,"bold"))
SpriteEn.grid(row=2,column=1,pady=10)
Dew=Label(coldDrinksFrame,text="Dew",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Dew.grid(row=3,column=0,sticky=W,padx=5)
DewEn=Entry(coldDrinksFrame,text="Dew",width=10,bd=5,textvariable=dew,font=("arial",12,"bold"))
DewEn.grid(row=3,column=1,pady=10)
Frooti=Label(coldDrinksFrame,text="Frooti",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
Frooti.grid(row=4,column=0,sticky=W,padx=5)
FrootiEn=Entry(coldDrinksFrame,text="Frooti",width=10,bd=5,textvariable=frooti,font=("arial",12,"bold"))
FrootiEn.grid(row=4,column=1,pady=10)
CocaCola=Label(coldDrinksFrame,text="CocaCola",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
CocaCola.grid(row=5,column=0,sticky=W,padx=5)
CocaColaEn=Entry(coldDrinksFrame,text="CocaCola",width=10,bd=5,textvariable=cocacola,font=("arial",12,"bold"))
CocaColaEn.grid(row=5,column=1,pady=20)

billFrame=LabelFrame(productFrame)
billFrame.grid(row=0,column=3)
billLabel=Label(billFrame,text="Billing",bg="gray20",fg="white",font=("arial",15,"bold"))
billLabel.pack(fill=X)

billScroll=Scrollbar(billFrame,orient=VERTICAL)
billScroll.pack(side=RIGHT,fill=Y)
billArea=Text(billFrame,width=100,height=20,bd=5,font=("arial",10,"bold"),yscrollcommand=billScroll.set)
billArea.pack()
billScroll.config(command=billArea.yview)

billMenuFrame=LabelFrame(root,text="Bill Menu",bg="gray20",fg="white",font=("arial",15,"bold"),bd=5)
billMenuFrame.pack(fill=X)

# Price
CosmeticPrice=Label(billMenuFrame,text="Cosmetic Price",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
CosmeticPrice.grid(row=0,column=0,sticky=W)
CosmeticPriceEn=Entry(billMenuFrame,font=("arial",12,"bold"),width=18,bd=5,state="readonly",textvariable=CosmeticPriceV)
CosmeticPriceEn.grid(row=0,column=1,padx=20,pady=10)
GroceryPrice=Label(billMenuFrame,text="Grocery Price",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
GroceryPrice.grid(row=1,column=0,sticky=W)
GroceryPriceEn=Entry(billMenuFrame,font=("arial",12,"bold"),width=18,bd=5,state="readonly",textvariable=GroceryPriceV)
GroceryPriceEn.grid(row=1,column=1,padx=20,pady=10)
ColdDrinkPrice=Label(billMenuFrame,text="Cold Drinks Price",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
ColdDrinkPrice.grid(row=2,column=0,sticky=W)
ColdDrinkPriceEn=Entry(billMenuFrame,font=("arial",12,"bold"),width=18,bd=5,state="readonly",textvariable=ColdDrinkPriceV)
ColdDrinkPriceEn.grid(row=2,column=1,padx=20,pady=10)

# Tax
CosmeticTax=Label(billMenuFrame,text="Cosmetic Tax",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
CosmeticTax.grid(row=0,column=2,sticky=W)
CosmeticTaxEn=Entry(billMenuFrame,font=("arial",12,"bold"),width=18,bd=5)
CosmeticTaxEn.grid(row=0,column=3,padx=20,pady=10)
GroceryTax=Label(billMenuFrame,text="Grocery Tax",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
GroceryTax.grid(row=1,column=2,sticky=W)
GroceryTaxEn=Entry(billMenuFrame,font=("arial",12,"bold"),width=18,bd=5)
GroceryTaxEn.grid(row=1,column=3,padx=20,pady=10)
ColdDrinkTax=Label(billMenuFrame,text="Cold Drinks Tax",bg="gray20",fg="white",font=("arial",12,"bold"),height=2)
ColdDrinkTax.grid(row=2,column=2,sticky=W)
ColdDrinkTaxEn=Entry(billMenuFrame,font=("arial",12,"bold"),width=18,bd=5)
ColdDrinkTaxEn.grid(row=2,column=3,padx=20,pady=10)


# Button
emailBtn=Button(billMenuFrame,text="Email",bg="gray20",fg="white",bd=5,width=8,font=("arial",15,"bold"))
emailBtn.grid(row=0,column=4,rowspan=3,padx=10,pady=20)
PrintBtn=Button(billMenuFrame,text="Print",bg="gray20",fg="white",bd=5,width=8,font=("arial",15,"bold"))
PrintBtn.grid(row=0,column=5,rowspan=3,padx=10,pady=20)
BillBtn=Button(billMenuFrame,text="Bill",bg="gray20",fg="white",bd=5,width=8,font=("arial",15,"bold"))
BillBtn.grid(row=0,column=6,rowspan=3,padx=10,pady=20)
TotalBtn=Button(billMenuFrame,text="Total",bg="gray20",fg="white",bd=5,width=8,font=("arial",15,"bold"),command=totalPrice)
TotalBtn.grid(row=0,column=7,rowspan=3,padx=10,pady=20)
ClearBtn=Button(billMenuFrame,text="Clear",bg="gray20",fg="white",bd=5,width=8,font=("arial",15,"bold"),command=Clear)
ClearBtn.grid(row=0,column=8,rowspan=3,padx=10,pady=10)


root.mainloop()