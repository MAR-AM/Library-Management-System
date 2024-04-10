from tkinter import *
from tkinter import ttk

root = Tk()
root.title('test scroll')
root.geometry("1600x800")

for thing in range(100):
    Button(root, text=f'button {thing} yo !').grid(row=thing, column=0, padx=10,pady=10)

main_fram = Frame(root)
main_fram.pack(fill=BOTH,expand=1)

my_canvas = Canvas(main_fram)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_sclor = ttk.Scrollbar(main_fram, orient=VERTICAL,command=my_canvas.yview)
my_sclor.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_sclor.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))


second_frame = Frame(my_canvas)

my_canvas.create_window((0,0),window=second_frame, anchor="nw")


root.mainloop()