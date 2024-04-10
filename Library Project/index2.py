from tkinter import *
from buy_2 import Buy_2
from tkinter import messagebox
import mysql.connector


class index:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # Title Label
        lbltitle = Label(self.root, text="MAR-AM Book Store ", bd=0, relief=RIDGE,bg="#EED2EE", fg="#8A2BE2", font=("Vivaldi", 25, "bold"),pady=20,padx=10,width=93)
        lbltitle.place(x=-970)

        fram = Frame(self.root,bg="#CDB5CD")
        fram.place(x=0,y=74,width=1550,height=600)

        lblMember = Label(fram,bg="#CDB5CD",text="There is no friend as loyal as a book.",font=("Vivaldi",24,"bold"),padx=480,pady=6,fg="#27408B")
        lblMember.grid(row=0,column=0,sticky=W)

        Frame_books=LabelFrame(fram,bd=4,relief=RIDGE,bg="#CDB5CD",fg="blue",font=("Palatino Linotype",17,"bold"))
        Frame_books.place(x=0,y=49,height=524,width=1279)

        Card_1 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_1.place(x=3, y=3, height=253, width=200)

        self.book1=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-1.png")
        lbl_book1=Label(Card_1,image=self.book1,bg="white",borderwidth=0)
        lbl_book1.place(x=25,y=8,width=140,height=180)
        lbl_book1=Label(Card_1,text="119.99 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book1.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_1,command=self.buy_book1 ,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)
        



        Card_2 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_2.place(x=216, y=3, height=253, width=200)

        self.book2=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\Book-3.png")
        lbl_book2=Label(Card_2,image=self.book2,bg='white',borderwidth=0)
        lbl_book2.place(x=25,y=8,width=140,height=180)
        lbl_book2=Label(Card_2,text="150.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book2.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_2,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)

        Card_3 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_3.place(x=431, y=3, height=253, width=200)

        self.book3=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-4.png")
        lbl_book3=Label(Card_3,image=self.book3,bg='white',borderwidth=0)
        lbl_book3.place(x=23,y=8,width=140,height=180)
        lbl_book3=Label(Card_3,text="150.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book3.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_3,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)

        Card_4 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_4.place(x=646, y=3, height=253, width=200)

        self.book4=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-5.png")
        lbl_book4=Label(Card_4,image=self.book4,bg='white',borderwidth=0)
        lbl_book4.place(x=23,y=8,width=140,height=180)
        lbl_book4=Label(Card_4,text="150.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book4.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_4,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)

        Card_5 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_5.place(x=859, y=3, height=253, width=200)

        self.book5=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-6.png")
        lbl_book5=Label(Card_5,image=self.book5,bg='white',borderwidth=0)
        lbl_book5.place(x=23,y=8,width=140,height=180)
        lbl_book5=Label(Card_5,text="150.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book5.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_5,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)
        

        Card_6 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_6.place(x=1069, y=3, height=253, width=200)

        self.book6=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-7.png")
        lbl_book6=Label(Card_6,image=self.book6,bg='white',borderwidth=0)
        lbl_book6.place(x=23,y=8,width=140,height=180)
        lbl_book6=Label(Card_6,text="150.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book6.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_6,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)

    


        Card_7 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_7.place(x=3, y=260, height=253, width=200)

        self.book7=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-8.png")
        lbl_book7=Label(Card_7,image=self.book7,bg='white',borderwidth=0)
        lbl_book7.place(x=20,y=8,width=140,height=180)
        lbl_book7=Label(Card_7,text="149.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book7.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_7,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)



        Card_8 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_8.place(x=216, y=260, height=253, width=200)

        self.book8=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-9.png")
        lbl_book8=Label(Card_8,image=self.book8,bg='white',borderwidth=0)
        lbl_book8.place(x=20,y=8,width=140,height=180)
        lbl_book8=Label(Card_8,text="149.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book8.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_8,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)



        




        Card_10 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_10.place(x=431, y=260, height=253, width=200)

        self.book10=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-10.png")
        lbl_book10=Label(Card_10,image=self.book10,bg='white',borderwidth=0)
        lbl_book10.place(x=20,y=8,width=140,height=180)
        lbl_book10=Label(Card_10,text="149.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book10.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_10,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)






        Card_11 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_11.place(x=646, y=260, height=253, width=200)

        self.book11=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-11.png")
        lbl_book11=Label(Card_11,image=self.book11,bg='white',borderwidth=0)
        lbl_book11.place(x=20,y=8,width=140,height=180)
        lbl_book11=Label(Card_11,text="149.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book11.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_11,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)





        Card_12 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_12.place(x=859, y=260, height=253, width=200)

        self.book12=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-12.png")
        lbl_book12=Label(Card_12,image=self.book12,bg='white',borderwidth=0)
        lbl_book12.place(x=20,y=8,width=140,height=180)
        lbl_book12=Label(Card_12,text="149.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book12.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_12,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)




        Card_13 = LabelFrame(Frame_books, padx=1,  bd=2, relief="groove", bg="white", fg="blue", font=("Palatino Linotype", 17, "bold"))
        Card_13.place(x=1069, y=260, height=253, width=200)

        self.book13=PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\Library Project\book-13.png")
        lbl_book13=Label(Card_13,image=self.book13,bg='white',borderwidth=0)
        lbl_book13.place(x=23,y=8,width=140,height=180)
        lbl_book13=Label(Card_13,text="149.00 DH",font=("terminal",15,"bold"),bg="white",borderwidth=0)
        lbl_book13.place(x=25,y=195,width=140)
        Buy_Now = Button (Card_13,text="Buy Now",font=("terminal",15,"bold"),bd=0,relief=RIDGE,fg="#8B668B",bg="white",activeforeground="#CDB5CD",activebackground="white",cursor="hand2",width=16)
        Buy_Now.place(x=25,y=213,width=140,height=30)

    

    def buy_book1(self):
                self.root=Toplevel(self.root)
                self.root= Buy_2(self.root)

    


    
        
       

if __name__ == "__main__":
    root = Tk()
    obj = index(root)
    root.mainloop()
