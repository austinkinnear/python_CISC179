import tkinter as tk
from tkinter import Label

class MyApp:
    def __init__(self, root):
        #Reference to parent window
        self.main_window = root
        # Created the label to be a child of sel.main_window as suggested
        self.label = Label(self.main_window, text="Programming is fun!")
        self.label.pack()

# Main window created with Tkinter, then the instance and then the event loop
root = tk.Tk()
app = MyApp(root)
root.mainloop()

