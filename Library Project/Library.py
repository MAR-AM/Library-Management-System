from tkinter import *
from tkinter import ttk
# import tkinter as tk
import mysql.connector
from tkinter import messagebox





class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title ("MAR-AM BOOK STORE")
        self.root.geometry("1600x800")

        
        # ==================== Variables ====================================
        
        self.TypeMember = StringVar()
        self.First_name_entry = StringVar()
        self.last_name_entry = StringVar()
        self.Sexe = StringVar()
        self.Aresse_entry = StringVar()
        self.Postal_Code_entry = StringVar()
        self.Code_CIN_entry = StringVar()
        self.Mobile_number_entry = StringVar()
        self.Book_id_entry = StringVar()
        self.Book_Title_entry = StringVar()
        self.Auther_Name_entry = StringVar()
        self.nbr_page_entry = StringVar()
        self.Edition_entry = StringVar()
        self.Date_purchase_entry = StringVar()
        self.Quantity_entry = StringVar()
        self.Price_entry = StringVar()

    
        lbltitle = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bd=12,relief=RIDGE,bg="black",fg="#9A32CD",font=("times new roman",30,"bold"),padx=2,pady=4)
        lbltitle.place(x=0,y=0,width=1280,height=95)

        
        self.img1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\logo-2.png")
        lblimg1=Label(image=self.img1,bg='black',borderwidth=0)
        lblimg1.place(x=100,y=20,width=180,height=60)


        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#838B8B")
        frame.place(x=0,y=95,width=1280,height=360)


        # ==================== First Frame left ======================



        DataFrameLeft=LabelFrame(frame,text = "Library Membership Information",bd=12,relief=RIDGE,bg="#838B8B",fg="blue",font=("Palatino Linotype",17,"bold"))
        DataFrameLeft.place(x=-15,y=0,height=330,width=790)

        lblMember = Label(DataFrameLeft,bg="#838B8B",text="Member Type : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        TypeMember = ttk.Combobox(DataFrameLeft,textvariable = self.TypeMember,font=("times new roman",12,"bold"),width=28,state="readonly")
        TypeMember["value"]=("Admin Staf","Student","Lecturer","Employee","Other")
        TypeMember.grid(row=0,column=1)


        First_name = Label(DataFrameLeft,bg="#838B8B",text="First Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        First_name.grid(row=1,column=0,sticky=W)
        First_name_entry=Entry(DataFrameLeft,textvariable=self.First_name_entry,font=("times new roman",15,"bold"),width=24)
        First_name_entry.grid(row=1,column=1,sticky=W)


        last_name = Label(DataFrameLeft,bg="#838B8B",text="Last Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        last_name.grid(row=2,column=0,sticky=W)
        last_name_entry=Entry(DataFrameLeft,textvariable=self.last_name_entry,font=("times new roman",15,"bold"),width=24)
        last_name_entry.grid(row=2,column=1,sticky=W)
        

        lblSexe = Label(DataFrameLeft,bg="#838B8B",text="Gender : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSexe.grid(row=3,column=0,sticky=W)
        Sexe = ttk.Combobox(DataFrameLeft,textvariable=self.Sexe,font=("times new roman",12,"bold"),width=28,state="readonly")
        Sexe["value"]=("Female","Male")
        Sexe.grid(row=3,column=1)


        Aresse = Label(DataFrameLeft,bg="#838B8B",text="Adresse : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Aresse.grid(row=4,column=0,sticky=W)
        Aresse_entry=Entry(DataFrameLeft,textvariable=self.Aresse_entry,font=("times new roman",15,"bold"),width=24)
        Aresse_entry.grid(row=4,column=1,sticky=W)


        Postal_Code = Label(DataFrameLeft,bg="#838B8B",text="Postal Code : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Postal_Code.grid(row=5,column=0,sticky=W)
        Postal_Code_entry=Entry(DataFrameLeft,textvariable=self.Postal_Code_entry,font=("times new roman",15,"bold"),width=24)
        Postal_Code_entry.grid(row=5,column=1,sticky=W)

        Code_CIN = Label(DataFrameLeft,bg="#838B8B",text="Code CIN : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Code_CIN.grid(row=6,column=0,sticky=W)
        Code_CIN_entry=Entry(DataFrameLeft,textvariable=self.Code_CIN_entry,font=("times new roman",15,"bold"),width=24)
        Code_CIN_entry.grid(row=6,column=1,sticky=W)


        Mobile_number = Label(DataFrameLeft,bg="#838B8B",text="Mobile Number : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Mobile_number.grid(row=7,column=0,sticky=W)
        Mobile_number_entry=Entry(DataFrameLeft,textvariable=self.Mobile_number_entry,font=("times new roman",15,"bold"),width=24)
        Mobile_number_entry.grid(row=7,column=1,sticky=W)



        # ===================== first Frame right==================


        Book_id = Label(DataFrameLeft,bg="#838B8B",text=" BooK id : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Book_id.grid(row=0,column=2,sticky=W)
        Book_id_entry=Entry(DataFrameLeft,textvariable=self.Book_id_entry,font=("times new roman",15,"bold"),width=24)
        Book_id_entry.grid(row=0,column=3,sticky=W)


        Book_Title = Label(DataFrameLeft,bg="#838B8B",text=" Book Title : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Book_Title.grid(row=1,column=2,sticky=W)
        Book_Title_entry=Entry(DataFrameLeft,textvariable=self.Book_Title_entry,font=("times new roman",15,"bold"),width=24)
        Book_Title_entry.grid(row=1,column=3,sticky=W)


        Auther_Name = Label(DataFrameLeft,bg="#838B8B",text=" Auther Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Auther_Name.grid(row=2,column=2,sticky=W)
        Auther_Name_entry=Entry(DataFrameLeft,textvariable=self.Auther_Name_entry,font=("times new roman",15,"bold"),width=24)
        Auther_Name_entry.grid(row=2,column=3,sticky=W)
        

        nbr_page = Label(DataFrameLeft,bg="#838B8B",text=" Number of pages : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        nbr_page.grid(row=3,column=2,sticky=W)
        nbr_page_entry=Entry(DataFrameLeft,textvariable=self.nbr_page_entry,font=("times new roman",15,"bold"),width=24)
        nbr_page_entry.grid(row=3,column=3,sticky=W)
        


        Edition = Label(DataFrameLeft,bg="#838B8B",text=" Edition : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Edition.grid(row=4,column=2,sticky=W)
        Edition_entry=Entry(DataFrameLeft,textvariable=self.Edition_entry,font=("times new roman",15,"bold"),width=24)
        Edition_entry.grid(row=4,column=3,sticky=W)


        Date_purchase = Label(DataFrameLeft,bg="#838B8B",text=" Date Purchase : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Date_purchase.grid(row=5,column=2,sticky=W)
        Date_purchase_entry=Entry(DataFrameLeft,textvariable=self.Date_purchase_entry,font=("times new roman",15,"bold"),width=24)
        Date_purchase_entry.grid(row=5,column=3,sticky=W)

        Quantity = Label(DataFrameLeft,bg="#838B8B",text=" Quantity : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Quantity.grid(row=6,column=2,sticky=W)
        Quantity_entry=Entry(DataFrameLeft,textvariable=self.Quantity_entry,font=("times new roman",15,"bold"),width=24)
        Quantity_entry.grid(row=6,column=3,sticky=W)


        Price = Label(DataFrameLeft,bg="#838B8B",text=" Price : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Price.grid(row=7,column=2,sticky=W)
        Price_entry=Entry(DataFrameLeft,textvariable=self.Price_entry,font=("times new roman",15,"bold"),width=24)
        Price_entry.grid(row=7,column=3,sticky=W)
 
        # ==================== Data Frame  ======================

        DataFrameRight = LabelFrame(frame, padx=2, text="Book Details", bd=12, relief="groove", bg="#838B8B", fg="blue", font=("Palatino Linotype", 17, "bold"))
        DataFrameRight.place(x=780, y=0, height=330, width=450)

        self.textBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=22, height=14, padx=5, pady=6)
        self.textBox.grid(row=0, column=2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")

        List_Books = ["• The Prophet", "• My Name is Red", "• The Great Gatsby", "• The Compound Effect", "• The Hobbit", "• The Miracle Morning",
                      "• Brave New World", "• The Hunger Games", "• Moby-Dick","• A Game of Thrones", "• The Power of Habit", "• Jane Eyre",
                      "• 1001 Nights","• The Sand Child","• Cities of Salt" ,"• The Dervish House","• Desert God",
                      "• Arabian Jazz","• Palace Walk","• The Dove's Necklace", "• Mirage", "• The Corsair","• The Map of Love" ,
                     ]
        

        def SelectBook(event=""):
            Value = str(list_Box.get(list_Box.curselection()))
            x = Value

            if ( x == "• The Prophet" ):
                self.Book_id_entry.set(9405832)
                self.Book_Title_entry.set("The Prophet")
                self.Auther_Name_entry.set("Kahlil Gibran")
                self.nbr_page_entry.set(150)
                self.Edition_entry.set("January 23, 2007")
                self.Date_purchase_entry.set("2018/02/23")
                self.Quantity_entry.set(1)
                self.Price_entry.set(90.99)
            elif ( x == "• My Name is Red" ):
                self.Book_id_entry.set(1234567)
                self.Book_Title_entry.set("My Name is Red")
                self.Auther_Name_entry.set("Orhan Pamuk")
                self.nbr_page_entry.set(300)
                self.Edition_entry.set("March 15, 2001")
                self.Date_purchase_entry.set("2019/05/10")
                self.Quantity_entry.set(1)
                self.Price_entry.set(120.00)

            




        list_Box = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=14, yscrollcommand=listScrollBar.set)
        list_Box.bind("<<ListboxSelect>>",SelectBook)
        list_Box.grid(row=0, column=0, padx=4)

        


        listScrollBar.config(command=list_Box.yview)

        for item in List_Books:
            list_Box.insert(END,item)


        # ==================== Buttons ======================
        
        frameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#838B8B")
        frameButton.place(x=0,y=450,width=1280,height=65)

        Add_Data = Button (frameButton,command=self.add_data,text="Add Data",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#68228B",cursor="hand2",width=16)
        Add_Data.grid(row=0, column=0)

        Show_Data = Button (frameButton,text="Show Data",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#68228B",cursor="hand2",width=16)
        Show_Data.grid(row=0, column=1)

        Update = Button (frameButton,text="Update",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=16)
        Update.grid(row=0, column=2)

        Delete = Button (frameButton,text="Delete",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=16)
        Delete.grid(row=0, column=3)

        Reset = Button (frameButton,text="Reset",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=16)
        Reset.grid(row=0, column=4)

        Exit = Button (frameButton,text="Exit",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=17)
        Exit.grid(row=0, column=5)

        # ==================== Information Fram======================
        
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#838B8B")
        FrameDetails.place(x=0, y=510, width=1280, height=140)

        table = Frame(FrameDetails, bd=6, relief=RIDGE, padx=20, bg="#838B8B")
        table.place(x=-20, y=0, width=1255, height=115)

        Table_scroll_X = ttk.Scrollbar(table, orient=HORIZONTAL)
        Table_scroll_Y = ttk.Scrollbar(table, orient=VERTICAL)

        self.library_table = ttk.Treeview(table, column=("Type Member", "First name", "Last name", "Gender", "Adresse", "Postal Code", "CodeCIN", "Mobile Number",
                                                          "Book id", "Book Title", "Auther Name", "nbr_page", "Edition", "Date Purchase", "Quantity", "Price"), xscrollcommand=Table_scroll_X.set, yscrollcommand=Table_scroll_Y.set)

        Table_scroll_X.pack(side=BOTTOM, fill=X)
        Table_scroll_Y.pack(side=RIGHT, fill=Y)

        Table_scroll_X.config(command=self.library_table.xview)
        Table_scroll_Y.config(command=self.library_table.yview)

        


        self.library_table.heading("Type Member",text="Member Type")
        self.library_table.heading("First name",text="First name")
        self.library_table.heading("Last name",text="Last name")
        self.library_table.heading("Gender",text="Gender")
        self.library_table.heading("Adresse",text="Adresse")
        self.library_table.heading("Postal Code",text="Postal Code")
        self.library_table.heading("CodeCIN",text="CodeCIN")
        self.library_table.heading("Mobile Number",text="Mobile Number")

        self.library_table.heading("Book id",text="Book id")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Auther Name",text="Auther Name")
        self.library_table.heading("nbr_page",text=" nbr_page")
        self.library_table.heading("Edition",text="Edition")
        self.library_table.heading("Date Purchase",text="Date Purchase")
        self.library_table.heading("Quantity",text="Quantity")
        self.library_table.heading("Price",text="Price")
        

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("Type Member",width=100)
        self.library_table.column("First name",width=100)
        self.library_table.column("Last name",width=100)
        self.library_table.column("Gender",width=100)
        self.library_table.column("Adresse",width=100)
        self.library_table.column("Postal Code",width=100)
        self.library_table.column("CodeCIN",width=100)
        self.library_table.column("Mobile Number",width=100)
        self.library_table.column("Book id",width=100)
        self.library_table.column("Book Title",width=100)
        self.library_table.column("Auther Name",width=100)
        self.library_table.column("nbr_page",width=100)
        self.library_table.column("Edition",width=100)
        self.library_table.column("Date Purchase",width=100)
        self.library_table.column("Quantity",width=100)
        self.library_table.column("Price",width=100)



    def add_data(self):
        Connect = mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="library")
        my_cursor = Connect.cursor()
        my_cursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.TypeMember.get(),
                            self.First_name_entry.get(),
                            self.last_name_entry.get(),
                            self.Sexe.get(),
                            self.Aresse_entry.get(),
                            self.Postal_Code_entry.get(),
                            self.Code_CIN_entry.get(),
                            self.Mobile_number_entry.get(),
                            self.Book_id_entry.get(),
                            self.Book_Title_entry.get(),
                            self.Auther_Name_entry.get(),
                            self.nbr_page_entry.get(),
                            self.Edition_entry.get(),
                            self.Date_purchase_entry.get(),
                            self.Quantity_entry.get(),
                            self.Price_entry.get()
                          ))
        Connect.commit()
        Connect.close() 

        messagebox.showinfo("Success","Member has been inserted successfully")






if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()