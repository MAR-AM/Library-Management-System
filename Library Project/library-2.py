from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import tkinter.messagebox
from datetime import datetime



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
        self.Book_Title_entry = StringVar()
        self.Auther_Name_entry = StringVar()
        self.nbr_page_entry = StringVar()
        self.Edition_entry = StringVar()
        self.Price_entry = StringVar()
        self.Date_purchase_entry = StringVar()
        self.Quantity_entry = StringVar()
        self.Final_price_entry = StringVar()
        

    
        lbltitle = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bd=12,relief=RIDGE,bg="black",fg="#9A32CD",font=("times new roman",30,"bold"),padx=2,pady=4)
        lbltitle.place(x=0,y=0,width=1280,height=95)

        
        self.img1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\logo-2.png")
        lblimg1=Label(self.root,image=self.img1,bg='black',borderwidth=0)
        lblimg1.place(x=100,y=20,width=180,height=60)


        self.img2=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-2.png")
        lblimg2=Label(self.root,image=self.img2,bg='black',borderwidth=0)
        lblimg2.place(x=1000,y=20,width=250,height=60)


        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#838B8B")
        frame.place(x=0,y=95,width=1280,height=360)


        # ==================== First Frame left ======================



        DataFrameLeft=LabelFrame(frame,text = "Library Membership Information",bd=10,relief=RIDGE,bg="#838B8B",fg="blue",font=("Palatino Linotype",17,"bold"))
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


        Book_Title = Label(DataFrameLeft,bg="#838B8B",text=" Book Title : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Book_Title.grid(row=0,column=2,sticky=W)
        Book_Title_entry=Entry(DataFrameLeft,textvariable=self.Book_Title_entry,font=("times new roman",15,"bold"),width=24)
        Book_Title_entry.grid(row=0,column=3,sticky=W)


        Auther_Name = Label(DataFrameLeft,bg="#838B8B",text=" Auther Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Auther_Name.grid(row=1,column=2,sticky=W)
        Auther_Name_entry=Entry(DataFrameLeft,textvariable=self.Auther_Name_entry,font=("times new roman",15,"bold"),width=24)
        Auther_Name_entry.grid(row=1,column=3,sticky=W)


        nbr_page = Label(DataFrameLeft,bg="#838B8B",text=" Number of pages : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        nbr_page.grid(row=2,column=2,sticky=W)
        nbr_page_entry=Entry(DataFrameLeft,textvariable=self.nbr_page_entry,font=("times new roman",15,"bold"),width=24)
        nbr_page_entry.grid(row=2,column=3,sticky=W)
        

        Edition = Label(DataFrameLeft,bg="#838B8B",text=" Edition : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Edition.grid(row=3,column=2,sticky=W)
        Edition_entry=Entry(DataFrameLeft,textvariable=self.Edition_entry,font=("times new roman",15,"bold"),width=24)
        Edition_entry.grid(row=3,column=3,sticky=W)
        


        Price = Label(DataFrameLeft,bg="#838B8B",text=" Price : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Price.grid(row=4,column=2,sticky=W)
        Price_entry=Entry(DataFrameLeft,textvariable=self.Price_entry,font=("times new roman",15,"bold"),width=24)
        Price_entry.grid(row=4,column=3,sticky=W)


        Date_purchase = Label(DataFrameLeft,bg="#838B8B",text=" Date Purchase : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Date_purchase.grid(row=5,column=2,sticky=W)
        Date_purchase_entry=Entry(DataFrameLeft,textvariable=self.Date_purchase_entry,font=("times new roman",15,"bold"),width=24)
        Date_purchase_entry.grid(row=5,column=3,sticky=W)

        Quantity = Label(DataFrameLeft,bg="#838B8B",text=" Quantity : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Quantity.grid(row=6,column=2,sticky=W)
        Quantity_entry=Entry(DataFrameLeft,textvariable=self.Quantity_entry,font=("times new roman",15,"bold"),width=24)
        Quantity_entry.grid(row=6,column=3,sticky=W)


        Final_price = Label(DataFrameLeft,bg="#838B8B",text=" Final price : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        Final_price.grid(row=7,column=2,sticky=W)
        Final_price_entry=Entry(DataFrameLeft,textvariable=self.Final_price_entry,font=("times new roman",15,"bold"),width=24)
        Final_price_entry.grid(row=7,column=3,sticky=W)
 
        # ==================== Data Frame  ======================

        DataFrameRight = LabelFrame(frame, padx=1, text="Book Details", bd=9, relief="groove", bg="#838B8B", fg="blue", font=("Palatino Linotype", 17, "bold"))
        DataFrameRight.place(x=780, y=0, height=330, width=230)


        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")

        List_Books = ["• The Prophet", "• My Name is Red", "• One Piece", "• The Compound Effect", "• The Hobbit", "• The Miracle Morning",
                      "• Brave New World", "• The Hunger Games", "• Moby-Dick","• A Game of Thrones", "• The Power of Habit", "• Jane Eyre",
                      "• 1001 Nights","• The Sand Child","• Cities of Salt" ,"• The Dervish House","• Desert God",
                      "• Arabian Jazz","• Palace Walk","• The Dove's Necklace", "• Mirage", "• The Corsair","• The Map of Love" ,
                     ]
        
        def get_current_date():
            return datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        
        def SelectBook( event = "" ):
            Value = str(list_Box.get(list_Box.curselection()))
            x = Value

            if ( x == "• The Prophet" ):
                self.Book_Title_entry.set("The Prophet")
                self.Auther_Name_entry.set("Kahlil Gibran")
                self.nbr_page_entry.set(150)
                self.Edition_entry.set("January 23, 2007")
                self.Price_entry.set(119.99)
                self.Date_purchase_entry.set(get_current_date())
                self.Quantity_entry.set(1)
                self.Final_price_entry.set(119.99)
                
            elif ( x == "• My Name is Red" ):
                self.Book_Title_entry.set("My Name is Red")
                self.Auther_Name_entry.set("Orhan Pamuk")
                self.nbr_page_entry.set(300)
                self.Edition_entry.set("March 15, 2001")
                self.Price_entry.set(150.00)
                self.Date_purchase_entry.set(get_current_date())
                self.Quantity_entry.set(2)
                self.Final_price_entry.set(300.00)

            elif ( x == "• One Piece" ):
                self.Book_Title_entry.set("One Piece")
                self.Auther_Name_entry.set("Eiichiro Oda")
                self.nbr_page_entry.set(200)
                self.Edition_entry.set("July 22, 1997")
                self.Price_entry.set(89.00)
                self.Date_purchase_entry.set(get_current_date())
                self.Quantity_entry.set(3)
                self.Final_price_entry.set(267.00)
            
            elif ( x == "• The Compound Effect" ):
                self.Book_Title_entry.set("The Compound Effect")
                self.Auther_Name_entry.set("Darren Hardy")
                self.nbr_page_entry.set(176)
                self.Edition_entry.set("October 2, 2012")
                self.Price_entry.set(129.99)
                self.Date_purchase_entry.set(get_current_date())
                self.Quantity_entry.set(5)
                self.Final_price_entry.set(649.95)


            



        list_Box = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=14, yscrollcommand=listScrollBar.set)
        list_Box.bind("<<ListboxSelect>>",SelectBook)
        list_Box.grid(row=0, column=0, padx=4)

        listScrollBar.config(command=list_Box.yview)

        for item in List_Books:
            list_Box.insert(END,item)


        # ==================== Buttons ======================
        

        Add_Data = Button (frame,command=self.add_data,text="Add Data",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#68228B",cursor="hand2",width=16)
        Add_Data.place(x=1018,y=11,width=210,height=45)


        # Show_Data = Button (frame,command=self.Showdata,text="Show Data",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#68228B",cursor="hand2",width=16)
        # Show_Data.place(x=1018,y=65,width=210,height=45)
        

        Update = Button (frame,command=self.Update,text="Update",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=16)
        Update.place(x=1018,y=120,width=210,height=45)

        Delete = Button (frame,command=self.delete,text="Delete",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=16)
        Delete.place(x=1018,y=175,width=210,height=45)

        Reset = Button (frame,command=self.reset,text="Reset",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="#A4D3EE",cursor="hand2",width=16)
        Reset.place(x=1018,y=230,width=210,height=45)

        Exit = Button (frame,text="Exit",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#1874CD",bg="black",activeforeground="white",activebackground="red",cursor="hand2",width=17,command=self.exit_1)
        Exit.place(x=1018,y=284,width=210,height=45)

        # ==================== Information Frame  ======================
        
        FrameDetails = Frame(self.root, bd=8, relief=RIDGE, padx=20, bg="#838B8B")
        FrameDetails.place(x=0, y=455, width=1280, height=193)

        style = ttk.Style()
        # style.theme_use('default')
        # style.configure("Treeview",background="#EBF5FB",foreground="black",rowheight=25,fieldbackground="D3D3D3")
        style.map('Treeview',background=[('selected',"#9A32CD")])
 
        table = Frame(FrameDetails, bd=4, relief=RIDGE, padx=20, bg="#838B8B")
        table.place(x=-20, y=0, width=1266, height=175)

        Table_scroll_X = ttk.Scrollbar(table, orient=HORIZONTAL)
        Table_scroll_Y = ttk.Scrollbar(table, orient=VERTICAL)

        self.library_table = ttk.Treeview(table, column=("Type Member", "First name", "Last name", "Gender", "Adresse", "Postal Code", "CodeCIN", "Mobile Number",
                                                         "Book Title", "Auther Name", "nbr_page", "Edition","Price", "Date Purchase", "Quantity", "Final Price"), xscrollcommand=Table_scroll_X.set, yscrollcommand=Table_scroll_Y.set)

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

        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Auther Name",text="Auther Name")
        self.library_table.heading("nbr_page",text=" nbr_page")
        self.library_table.heading("Edition",text="Edition")
        self.library_table.heading("Price",text="Price")
        self.library_table.heading("Date Purchase",text="Date Purchase")
        self.library_table.heading("Quantity",text="Quantity")
        self.library_table.heading("Final Price",text="Final Price")
        

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("Type Member",width=100)
        self.library_table.column("First name",width=100)
        self.library_table.column("Last name",width=100)
        self.library_table.column("Gender",width=100)
        self.library_table.column("Adresse",width=160)
        self.library_table.column("Postal Code",width=100)
        self.library_table.column("CodeCIN",width=100)
        self.library_table.column("Mobile Number",width=100)
        self.library_table.column("Book Title",width=100)
        self.library_table.column("Auther Name",width=100)
        self.library_table.column("nbr_page",width=100)
        self.library_table.column("Edition",width=100)
        self.library_table.column("Price",width=100)
        self.library_table.column("Date Purchase",width=100)
        self.library_table.column("Quantity",width=100)
        self.library_table.column("Final Price",width=100)


        self.fetchAll_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)



    def add_data(self):
        if self.TypeMember.get()=='':
            messagebox.showerror("Error","All field are required")
        else:
            Connect = mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="Library")
            my_cursor = Connect.cursor()
            my_cursor.execute("insert into data_library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.TypeMember.get(),
                            self.First_name_entry.get(),
                            self.last_name_entry.get(),
                            self.Sexe.get(),
                            self.Aresse_entry.get(),
                            self.Postal_Code_entry.get(),
                            self.Code_CIN_entry.get(),
                            self.Mobile_number_entry.get(),
                            self.Book_Title_entry.get(),
                            self.Auther_Name_entry.get(),
                            self.nbr_page_entry.get(),
                            self.Edition_entry.get(),
                            self.Price_entry.get(),
                            self.Date_purchase_entry.get(),
                            self.Quantity_entry.get(),
                            self.Final_price_entry.get()
                          ))
            Connect.commit()
            self.fetchAll_data()
            Connect.close() 

            messagebox.showinfo("Success","Member has been inserted successfully")



    def fetchAll_data(self):
        Connect = mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="Library")
        my_cursor = Connect.cursor()
        my_cursor.execute("Select * from data_library") 
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            Connect.commit()
        Connect.close()



    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.TypeMember.set(row[0]),
        self.First_name_entry.set(row[1]),
        self.last_name_entry.set(row[2]),
        self.Sexe.set(row[3]),
        self.Aresse_entry.set(row[4]),
        self.Postal_Code_entry.set(row[5]),
        self.Code_CIN_entry.set(row[6]),
        self.Mobile_number_entry.set(row[7]),
        self.Book_Title_entry.set(row[8]),
        self.Auther_Name_entry.set(row[9]),
        self.nbr_page_entry.set(row[10]),
        self.Edition_entry.set(row[11]),
        self.Price_entry.set(row[12]),
        self.Date_purchase_entry.set(row[13]),
        self.Quantity_entry.set(row[14]),
        self.Final_price_entry.set(row[15])



    def Showdata (self):
        print("coco")



    def reset(self):
        self.TypeMember.set(""),
        self.First_name_entry.set(""),
        self.last_name_entry.set(""),
        self.Sexe.set(""),
        self.Aresse_entry.set(""),
        self.Postal_Code_entry.set(""),
        self.Code_CIN_entry.set(""),
        self.Mobile_number_entry.set(""),
        self.Book_Title_entry.set(""),
        self.Auther_Name_entry.set(""),
        self.nbr_page_entry.set(""),
        self.Edition_entry.set(""),
        self.Price_entry.set(""),
        self.Date_purchase_entry.set(""),
        self.Quantity_entry.set(""),
        self.Final_price_entry.set("")



    def exit_1 (self):
        iExit= tkinter.messagebox.askyesno("Library Management Systeme","Do you want to exit")
        if iExit > 0:
            self.root.destroy()
            return
    


    def delete(self):
        if self.Code_CIN_entry.get() == "" or self.Book_Title_entry.get() == "":
            messagebox.showwarning("Error", "First select the member")
        else:
            Connect = mysql.connector.connect(host="localhost", user="Mama", password="Mama@123@", database="Library")
            my_cursor = Connect.cursor()
            query = "DELETE FROM data_library WHERE Code_CIN = %s AND Book_Title = %s"
            values = (self.Code_CIN_entry.get(), self.Book_Title_entry.get())
            my_cursor.execute(query, values)
            Connect.commit()
            self.fetchAll_data()
            self.reset()
            Connect.close()
            messagebox.showinfo("Success", "Member has been Deleted")
   


    def Update(self):
        if self.Code_CIN_entry.get() == "" or self.Book_Title_entry.get() == "":
            messagebox.showwarning("Error", "First select the member")
        else:
            Connect = mysql.connector.connect(host="localhost", user="Mama", password="Mama@123@", database="Library")
            my_cursor = Connect.cursor()
            query = "UPDATE data_library SET Member_type = %s, First_name = %s, Last_Name = %s, Gender = %s, Adresse = %s, Postal_Code = %s, Code_CIN = %s, Mobile_Number = %s, Book_Title = %s, Auther_Name = %s, nbr_page = %s, Edition = %s, price = %s, Date_purchase = %s, Quantity = %s, Final_price = %s WHERE Code_CIN = %s AND Book_Title = %s"
            values = (
                            self.TypeMember.get(),
                            self.First_name_entry.get(),
                            self.last_name_entry.get(),
                            self.Sexe.get(),
                            self.Aresse_entry.get(),
                            self.Postal_Code_entry.get(),
                            self.Code_CIN_entry.get(),
                            self.Mobile_number_entry.get(),
                            self.Book_Title_entry.get(),
                            self.Auther_Name_entry.get(),
                            self.nbr_page_entry.get(),
                            self.Edition_entry.get(),
                            self.Price_entry.get(),
                            self.Date_purchase_entry.get(),
                            self.Quantity_entry.get(),
                            self.Final_price_entry.get(),
                            self.Code_CIN_entry.get(),
                            self.Book_Title_entry.get()
                     )
            my_cursor.execute(query, values)
            Connect.commit()
            self.fetchAll_data()
            self.reset()
            Connect.close()
            messagebox.showinfo("Success", "Member has been Updated")







if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()