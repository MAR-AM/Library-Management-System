from tkinter import *
from PIL import Image,ImageTk


class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        lbltitle = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                         ,bg="white",fg="blue",font=("times new roman",30,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        # Load the image and resize it
        img1 = PhotoImage(file='C:\\Users\\user\\OneDrive\\Desktop\\Library Project\\1.png')
        img1 = img1.subsample(1)
        background_label = Label(root, image=img1)
        background_label.place(x=70, y=20)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)

        


        img1=Image.open(r"C:\Users\user\OneDrive\Desktop\Library Project\1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=9,width=1550,height=140)




if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()



# from tkinter import *

# class LibraryManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Library Management System")
#         self.root.geometry("1550x800+0+0")
        
#         # Title Label
#         lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
#                          bg="white", fg="blue", font=("times new roman", 30, "bold"), padx=2, pady=4)
#         lbltitle.pack(side=TOP, fill=X)

#         # Load the image and resize it
#         img1 = PhotoImage(file='C:\\Users\\user\\OneDrive\\Desktop\\Library Project\\1.png')
#         img1 = img1.subsample(1)

#         # Image Label
#         img_label = Label(self.root, image=img1, bd=4, relief=RIDGE)
#         img_label.place(x=70, y=90)  # Adjust the position as needed

# if __name__ == "__main__":
#     root = Tk()
#     obj = LibraryManagementSystem(root)
#     root.mainloop()
