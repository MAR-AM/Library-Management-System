from tkinter import *

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # Title Label
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                         bg="white", fg="blue", font=("times new roman", 30, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        # Load the image
        img1 = PhotoImage(file='C:\\Users\\user\\OneDrive\\Desktop\\Library Project\\1.png')

        # Image Label
        img_label = Label(self.root, image=img1)
        img_label.image = img1  # Keep a reference to the image
        img_label.pack(side=RIGHT, padx=10, pady=10)  # Adjust the padding as needed

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()


