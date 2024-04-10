import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Example usage
class MyApp(tk.Tk):
    def __init__(self,root):
        self.root = root
        self.title("Scrollable Tkinter Frame")
        self.geometry("400x300")

        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.pack(side="top", fill="both", expand=True)
        
        for i in range(50):
            tk.Label(self.scrollable_frame.scrollable_frame, text=f"Label {i}").pack()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
