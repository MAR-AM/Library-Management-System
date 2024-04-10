from tkinter import *
from tkinter import messagebox
from register import *
import mysql.connector
# from libraryWithScroll import LibraryManagementSystem
from index2 import index
 


class Login_window:
    def __init__(self, root):
        self.window = root
        self.window.title('Login')
        self.window.geometry("1550x800+0+0")

        self.bg = PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\books-1.png")
        lbl_bg=Label(self.window,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        fram = Frame(self.window,bg="white")
        fram.place(x=475,y=100,width=340,height=450)

        self.img1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\User-library.png")
        lblimg1=Label(self.window,image=self.img1,bg='white',borderwidth=0)
        lblimg1.place(x=600,y=105,width=100,height=100) 

        get_str = Label(fram,text="Get Started",font=("Impact",25,"bold"),fg="#7D26CD",bg="white")
        get_str.place(x=90,y=100)

        #Labels
        username=Label(fram,text=" Username : ",font=("times new roman",15,"bold"),fg="#8B668B",bg="white")
        username.place(x=50,y=155)

        self.textuser = Entry(fram,font=("times new roman",15,"bold"),bg="#F5FFFA")
        self.textuser.place(x=20,y=185,width=300)

        password=Label(fram,text=" Password : ",font=("times new roman",15,"bold"),fg="#8B668B",bg="white")
        password.place(x=50,y=225)

        self.textpass = Entry(fram,show="•",font=("times new roman",15,"bold"),bg="#F5FFFA")
        self.textpass.place(x=20,y=250,width=300)

        # ================ Icon images ===============
        

        self.img2=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\User-library--icon.png")
        lblimg2=Label(self.window,image=self.img2,bg='white',borderwidth=0)
        lblimg2.place(x=500,y=260,width=20,height=20)

        self.img3=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\psw1-removebg-preview.png")
        lblimg3=Label(self.window,image=self.img3,bg='white',borderwidth=0)
        lblimg3.place(x=490,y=325,width=40,height=25)

        # ================ buttons ===============

        #Login button
        loginBtn = Button(fram,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#FFD700",activeforeground="white",activebackground="#A4D3EE",cursor="hand2")
        loginBtn.place(x=80,y=300,width=180,height=35)
        
        # register BUtton
        registerBtn = Button(fram,text="New User register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="#6495ED",bg="white",activeforeground="#8B795E",activebackground="white",cursor="hand2")
        registerBtn.place(x=7,y=360,width=160)

        # forget_PSW_btn
        ForgetPSW_Btn = Button(fram,command=self.forget_psw,text="  Forget Password ?",font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="#6495ED",bg="white",activeforeground="#CDBE70",activebackground="white",cursor="hand2")
        ForgetPSW_Btn.place(x=2,y=400,width=160) 

    def register_window(self):
        self.new_window=Toplevel(self.window)
        self.app=Register(self.new_window)


    def login(self):
        if self.textuser.get()=="" and self.textpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="" :
            messagebox.showerror("Error"," User field required")
        elif self.textpass.get()=="":
            messagebox.showerror("Error"," Password field required")
        elif self.textuser.get()=="ana" and self.textpass.get()=="123":
            messagebox.showinfo("Success","Welcome to MAR-AM BOOK STORE")
        else:
            # messagebox.showerror("Invalid","Invalid Username & Password")
            conn=mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="library")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and new_psw=%s",(
                self.textuser.get(),
                self.textpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Check your Username & Password")
            else:
                # open_main=messagebox.askyesno("YesNo","Access only admin")
                open_main = messagebox.showinfo("Success","Welcome to MAR-AM BOOK STORE")
                if open_main:
                    self.window=Toplevel(self.window)
                    self.window=index(self.window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ===========================update password ==============================
    def update_psw(self):
        if self.contact_entry.get()=="" and self.newPSW_entry.get()=="" and self.Confirm_newPSW_entry.get()=="" :
            messagebox.showerror("Error","All fields are required")
        elif self.contact_entry.get()=="":
            messagebox.showerror("Error","Please enter your Contact number")
        elif self.newPSW_entry.get()=="":
            messagebox.showerror("Error","Please enter your New Password")
        elif self.Confirm_newPSW_entry.get()=="":
            messagebox.showerror("Error","Please enter your Confirm Password")
        elif self.newPSW_entry.get()!=self.Confirm_newPSW_entry.get():
            messagebox.showerror("Error","Password & Confirm password must be Same")
        else:
            conn=mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="library")
            my_cursor = conn.cursor()
            query1=("select * from register where email=%s and contact=%s ")
            value1=(self.textuser.get(),self.contact_entry.get())
            my_cursor.execute(query1,value1)
            row=my_cursor.fetchone()
            if row ==None:
                messagebox.showerror("Error","Please enter correct Contact number")
            else:
                query2=("update register set new_psw=%s where email=%s")
                value2=(self.Confirm_newPSW_entry.get(),self.textuser.get())
                my_cursor.execute(query2,value2)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","    Your password has been reset \n\n please login with the new password")   


    # =========================Forget password window=======================
    def forget_psw (self):
        if self.textuser.get()=='':
            messagebox.showerror("Error","Please Enter the Email adress to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="Mama",password="Mama@123@",database="library")
            my_cursor = conn.cursor()
            query=('select * from register where email=%s')
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter a valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x490+450+80")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg='#8B0000')
                l.place(x=0,y=10,relwidth=1)

                contact=Label(self.root2,text="Contact  Nº",font=("times new roman",16,"bold"),)
                contact.place(x=30,y=100)
                self.contact_entry=Entry(self.root2,font=("times new roman",15,"bold"))
                self.contact_entry.place(x=30,y=130,width=250)

                newPSW=Label(self.root2,text="New Password",font=("times new roman",16,"bold"))
                newPSW.place(x=30,y=200)
                self.newPSW_entry=Entry(self.root2,font=("times new roman",15,"bold"))
                self.newPSW_entry.place(x=30,y=230,width=250)

                Confirm_newPSW=Label(self.root2,text="Confirm Password",font=("times new roman",16,"bold"))
                Confirm_newPSW.place(x=30,y=300)

                self.Confirm_newPSW_entry=Entry(self.root2,font=("times new roman",15,"bold"))
                self.Confirm_newPSW_entry.place(x=30,y=330,width=250)

                btn=Button(self.root2,command=self.update_psw,text="Update Password",font=("times new roman",15,"bold"),fg="#388E8E",bg="#CDB5CD")
                btn.place(x=120,y=400)




if __name__ == "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()