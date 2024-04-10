from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from Library import LibraryManagementSystem
from LoginWhite import *



class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        # ===================== bg image =================

        self.bg = PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\books-1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1) 


        # ===================== left image =================
        # self.bg1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\regesterimg.png")
        # left_lbl=Label(self.root,image=self.bg1)
        # left_lbl.place(x=50,y=100,width=390,height=450)


        # ===================== main Frame =================
        frame = Frame (self.root,bg="white")
        frame.place(x=161,y=100,width=1000,height=450)
        register_lbl=Label(frame,text="Register HERE",font=("times new roman",20,"bold"),fg="#1874CD",bg="white")
        register_lbl.place(x=20,y=20)

        self.img2=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\register-pic2.png")
        lblimg2=Label(frame,image=self.img2,bg="white",borderwidth=0)
        lblimg2.place(x=710,y=35)

        # ===================== label and entry =================
        # --------------> row 1

        name=Label(frame,text="First Name",font=("times new roman",16,"bold"),bg="white")
        name.place(x=20,y=80)

        self.name_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.name_entry.place(x=20,y=110,width=250)

        last_name=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="white")
        last_name.place(x=400,y=80)

        self.last_name_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.last_name_entry.place(x=400,y=110,width=250)

        # --------------> row 2

        contact=Label(frame,text="Contact  Nº",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=20,y=160)

        self.contact_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=20,y=190,width=250)

        email=Label(frame,text="Email",font=("times new roman",16,"bold"),bg="white")
        email.place(x=400,y=160)

        self.email_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.email_entry.place(x=400,y=190,width=250)

        # --------------> row 3

        New_psw=Label(frame,text="Password",font=("times new roman",16,"bold"),bg="white")
        New_psw.place(x=20,y=250)

        self.New_psw_entry=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.New_psw_entry.place(x=20,y=280,width=250)

        Confirm=Label(frame,text="Confirm Password",font=("times new roman",16,"bold"),bg="white")
        Confirm.place(x=400,y=250)

        self.Confirm_entry=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.Confirm_entry.place(x=400,y=280,width=250)


        # =================== Check button =================
        self.var_check = IntVar() 
        self.Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",11,"bold"),onvalue=1,offvalue=0,cursor="hand2")
        self.Checkbtn.place(x=20,y=400,height=30)

        def toggle_password():
            if show_password_var.get():
                self.New_psw_entry.config(show="")
                self.Confirm_entry.config(show="")
            else:
                self.New_psw_entry.config(show="*")
                self.Confirm_entry.config(show="*")

        
        # Create a variable to hold the state of the checkbox
        show_password_var = IntVar()
        # Create the checkbox for toggling password visibility
        show_password_checkbox = Checkbutton(frame,font=("times new roman",11,"bold"), text="Show Password 👀", variable=show_password_var, command=toggle_password,cursor="hand2")
        show_password_checkbox.place(x=20,y=350)

        # =================== buttons =================
        RegisterBtn = Button(frame,command=self.register_data,text="Register Now",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#388E8E",bg="#CDB5CD",activeforeground="white",activebackground="#A4D3EE",cursor="hand2")
        RegisterBtn.place(x=720,y=300,width=250,height=45)

        login_Btn = Button(frame,command=self.Login_btn,text="Login Now",font=("times new roman",15,"bold"),bd=1,relief=RIDGE,fg="#388E8E",bg="#CDB5CD",activeforeground="white",activebackground="#A4D3EE",cursor="hand2")
        login_Btn.place(x=720,y=380,width=250,height=45)

    # =================== Function declaration =================
    
    def register_data(self):
        if self.name_entry.get() == "" and self.email_entry.get()=="" and self.last_name_entry.get()=="" and self.contact_entry.get()=="" and self.New_psw_entry.get()=="" and self.Confirm_entry.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.name_entry.get() == "" or self.email_entry.get()=="" or self.last_name_entry.get()=="" or self.contact_entry.get()=="" or self.New_psw_entry.get()=="" or self.Confirm_entry.get()=="":
            messagebox.showerror("Error","Some fields are required")
        elif self.New_psw_entry.get()!=self.Confirm_entry.get():
            messagebox.showerror("Error","Password & Confirm password must be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree Our terms & conditions")
        else:
            
            conn=mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="library")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.email_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                    self.name_entry.get(),
                    self.last_name_entry.get(),
                    self.contact_entry.get(),
                    self.email_entry.get(),
                    self.New_psw_entry.get(),
                    self.Confirm_entry.get()
                    
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","\tRegister Successfully\n\n Welcome to MAR-AM BOOK STORE")   

        self.name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.contact_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.New_psw_entry.delete(0, 'end')
        self.Confirm_entry.delete(0, 'end')

    def Login_btn(self):
        
                self.root=Toplevel(self.root)
                self.root=Login_window(self.root)

if __name__ == "__main__":
    root=Tk()
    app = Register(root)
    root.mainloop()


















    