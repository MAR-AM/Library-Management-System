from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry("1550x800+0+0")

        self.bg = PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\digital-books2-1030x473.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        fram = Frame(self.root,bg="black")
        fram.place(x=475,y=100,width=340,height=450)

        self.img1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\User-library.png")
        lblimg1=Label(image=self.img1,bg='black',borderwidth=0)
        lblimg1.place(x=600,y=105,width=100,height=100) 

        get_str = Label(fram,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        #Labels
        username=Label(fram,text=" Username : ",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=50,y=155)

        self.textuser = Entry(fram,font=("times new roman",15,"bold"))
        self.textuser.place(x=20,y=185,width=300)

        password=Label(fram,text=" Password : ",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=50,y=225)

        self.textpass = Entry(fram,font=("times new roman",15,"bold"))
        self.textpass.place(x=20,y=250,width=300)

        # ================ Icon images ===============
        

        self.img2=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\User-library--icon.png")
        lblimg2=Label(image=self.img2,bg='black',borderwidth=0)
        lblimg2.place(x=500,y=260,width=20,height=20)

        self.img3=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\psw-icon.png")
        lblimg3=Label(image=self.img3,bg='black',borderwidth=0)
        lblimg3.place(x=490,y=325,width=40,height=25)

        # ================ buttons ===============

        #Login button
        loginBtn = Button(fram,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#FFD700",activeforeground="white",activebackground="#A4D3EE",cursor="hand2")
        loginBtn.place(x=110,y=300,width=120,height=35)
        
        # register BUtton
        registerBtn = Button(fram,text="New User register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
        registerBtn.place(x=7,y=360,width=160)

        # forget_PSW_btn
        ForgetPSW_Btn = Button(fram,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
        ForgetPSW_Btn.place(x=2,y=400,width=160) 

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
            messagebox.showerror("Invalid","Invalid Username & Password")








if __name__ == "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()