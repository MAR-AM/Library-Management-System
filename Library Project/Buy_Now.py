from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



class Buy:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        self.TypeMember = StringVar()
        self.First_name_entry = StringVar()
        self.last_name_entry = StringVar()
        self.Sexe = StringVar()
        self.Aresse_entry = StringVar()
        self.Postal_Code_entry = StringVar()
        self.Code_CIN_entry = StringVar()
        self.Mobile_number_entry = StringVar()
        self.Book_Title_entry = StringVar(value="The Prophet")
        self.Quantity_entry = StringVar()
        self.Price_entry = StringVar()  
        
        # Title Label
        lbltitle = Label(self.root, text="MAR-AM Book Store ", bd=0, relief=RIDGE,bg="#EED2EE", fg="#8A2BE2", font=("Vivaldi", 25, "bold"),pady=20,padx=10,width=93)
        lbltitle.place(x=-970)

        fram = Frame(self.root,bg="#CDB5CD")
        fram.place(x=0,y=74,width=1550,height=600)

        titre = Label(fram,bg="#CDB5CD",text="There is no friend as loyal as a book.",font=("Vivaldi",24,"bold"),padx=480,pady=6,fg="#27408B")
        titre.grid(row=0,column=0,sticky=W)

        Frame_Buy_Now=LabelFrame(fram,bd=4,relief=RIDGE,bg="#CDB5CD",fg="blue",font=("Palatino Linotype",17,"bold"))
        Frame_Buy_Now.place(x=190,y=70,height=470,width=879)

        self.img1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\Buy_Now-1.png")
        lblimg1=Label(Frame_Buy_Now,image=self.img1,bg="#CDB5CD",borderwidth=0)
        lblimg1.place(x=350,y=10)




        lblMember = Label(Frame_Buy_Now,bg="#CDB5CD",text="Member Type : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        lblMember.place(x=0,y=101,width=210,height=25)

        TypeMember = ttk.Combobox(Frame_Buy_Now,textvariable = self.TypeMember,font=("times new roman",16,"bold"),width=28,state="readonly")
        TypeMember["value"]=("Admin Staf","Student","Lecturer","Employee","Other")
        TypeMember.place(x=220,y=101,width=310,height=30)



        First_name = Label(Frame_Buy_Now,bg="#CDB5CD",text="First Name : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=20)
        First_name.place(x=0,y=141,width=210,height=30)
        First_name_entry=Entry(Frame_Buy_Now,textvariable=self.First_name_entry,font=("times new roman",16,"bold"),width=24)
        First_name_entry.place(x=220,y=141,width=310,height=30)


        last_name = Label(Frame_Buy_Now,bg="#CDB5CD",text="Last Name : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=26)
        last_name.place(x=0,y=181,width=210,height=30)
        last_name_entry=Entry(Frame_Buy_Now,textvariable=self.last_name_entry,font=("times new roman",16,"bold"),width=24)
        last_name_entry.place(x=220,y=181,width=310,height=30)
        

        lblSexe = Label(Frame_Buy_Now,bg="#CDB5CD",text="Gender : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=26)
        lblSexe.place(x=0,y=221,width=210,height=30)
        Sexe = ttk.Combobox(Frame_Buy_Now,textvariable=self.Sexe,font=("times new roman",16,"bold"),width=28,state="readonly")
        Sexe["value"]=("Female","Male")
        Sexe.place(x=220,y=220,width=310,height=30)


        # Aresse = Label(Frame_Buy_Now,bg="#CDB5CD",text="city : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        # Aresse.place(x=0,y=256,width=210,height=30)
        # Aresse_entry=Entry(Frame_Buy_Now,textvariable=self.Aresse_entry,font=("times new roman",16,"bold"),width=24)
        # Aresse_entry.place(x=220,y=260,width=310,height=30)


        City = Label(Frame_Buy_Now,bg="#CDB5CD",text="Address",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        City.place(x=0,y=260,width=210,height=30)
        City_entry=Entry(Frame_Buy_Now,textvariable=self.Aresse_entry,font=("times new roman",16,"bold"),width=30)
        City_entry.place(x=220,y=260,width=310,height=30)

        Code_CIN = Label(Frame_Buy_Now,bg="#CDB5CD",text="Postal Code : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        Code_CIN.place(x=0,y=300,width=210,height=30)
        Code_CIN_entry=Entry(Frame_Buy_Now,textvariable = self.Postal_Code_entry,font=("times new roman",15,"bold"),width=24)
        Code_CIN_entry.place(x=220,y=300,width=310,height=30)


        Mobile_number = Label(Frame_Buy_Now,bg="#CDB5CD",text="Code CIN : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        Mobile_number.place(x=0,y=340,width=210,height=30)
        Mobile_number_entry=Entry(Frame_Buy_Now,textvariable=self.Code_CIN_entry,font=("times new roman",16,"bold"),width=24)
        Mobile_number_entry.place(x=220,y=340,width=310,height=30)

        Book_Title = Label(Frame_Buy_Now,bg="#CDB5CD",text="Mobile Number : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        Book_Title.place(x=0,y=380,width=210,height=30)
        Book_Title_entry=Entry(Frame_Buy_Now,textvariable = self.Mobile_number_entry,font=("times new roman",16,"bold"),width=24)
        Book_Title_entry.place(x=220,y=380,width=310,height=30)


        Quantite = Label(Frame_Buy_Now,bg="#CDB5CD",text="Book Title: ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        Quantite.place(x=0,y=420,width=210,height=30)
        Quantite_entry_entry=Entry(Frame_Buy_Now,textvariable = self.Book_Title_entry,font=("times new roman",16,"bold"),width=24,state="readonly")
        Quantite_entry_entry.place(x=220,y=420,width=310,height=30)


        final_price = Label(Frame_Buy_Now,bg="#CDB5CD",text="Final Price : ",font=("times new roman",16,"bold"),fg="#483D8B",padx=2,pady=6)
        final_price.place(x=610,y=250,width=130,height=30)
        total = 149.99 
        # if Quantite_entry_entry ==  1:
        #     total = 149.99
        # else:
        #     total = 149.99 * Quantite_entry_entry

        final_price_entry=Label(Frame_Buy_Now,text=(total,"DH"),font=("times new roman",16),bg="#CDB5CD",width=24)
        final_price_entry.place(x=730,y=250,width=130,height=30)

        self.img2=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\sella.png")
        lblimg2=Label(Frame_Buy_Now,image=self.img2,bg="#CDB5CD",borderwidth=0)
        lblimg2.place(x=610,y=55)

        Confirm = Button (Frame_Buy_Now,command=self.confirmation,text="Confirmation",font=("times new roman",18,"italic"),bd=1,relief=RIDGE,fg="#388E8E",bg="#CDB5CD",activeforeground="white",activebackground="red",cursor="hand2",width=17)
        Confirm.place(x=618,y=330,width=220,height=45)

        Exit = Button (Frame_Buy_Now,text="Exit",font=("times new roman",18,"italic"),bd=1,relief=RIDGE,fg="#8B0000",bg="#CDB5CD",activeforeground="white",activebackground="red",cursor="hand2",width=17,command=root.quit)
        Exit.place(x=618,y=410,width=220,height=45)

    def confirmation(self):
        
        if self.TypeMember.get()=='':
            messagebox.showerror("Error","All field are required")
        else:
            Connect = mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="Library")
            my_cursor = Connect.cursor()
            my_cursor.execute("INSERT INTO client (Member_type, First_name, Last_Name, Gender, Adresse, Postal_Code, Code_CIN, Mobile_number, Book_Title) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
    self.TypeMember.get(),
    self.First_name_entry.get(),
    self.last_name_entry.get(),
    self.Sexe.get(),
    self.Aresse_entry.get(),
    self.Postal_Code_entry.get(),
    self.Code_CIN_entry.get(),
    self.Mobile_number_entry.get(),
    self.Book_Title_entry.get()
))

            Connect.commit()
            Connect.close() 

            messagebox.showinfo("Success","Member has been inserted successfully")







if __name__ == "__main__":
    root = Tk()
    obj = Buy(root)
    root.mainloop()