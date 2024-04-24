import tkinter as tk
from tkinter import Label

class MyApp:
    def __init__(self, root):
        self.main_window = root
        self.label1 = Label(self.main_window, text="Label 1")
        # Packs self.label1 all the way to the left
        self.label1.pack(side="top", anchor="w")
        # Same thing but for self.label2 to be far left and below label1
        self.label2 = Label(self.main_window, text="Label 2")
        self.label2.pack(side="top", anchor="w")

root = tk.Tk()
root.title("Austin Kinnear")
root.geometry("300x100")
app = MyApp(root)
root.mainloop()


