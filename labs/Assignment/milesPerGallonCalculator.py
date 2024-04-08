import tkinter as tk
from tkinter import messagebox

# Function to calculte MPG to output to the messagebox
def calculate_mpg():
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        mpg = miles / gallons
        # Resuult given with MPG Result as title, and the solution only going to two decimals
        messagebox.showinfo("MPG Result", f"The car can drive {mpg: .2f} miles per gallon of gas.")

# Creates the main window with tkinter
root = tk.Tk()
# Title for window 
root.title("MPG Calculator") 

# Gallons input for GUI interface
tk.Label(root, text="Gallons of gas the car holds:").grid(row=0, column=0) 
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=0, column=1)

# Miles input for GUI 
tk.Label(root, text="Number of miles on a full tank:").grid(row=1, column=0)
miles_entry = tk.Entry(root)
miles_entry.grid(row=1, column=1)

# MPG button connected to out calculation function
calculate_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calculate_button.grid(row=2, column=0, columnspan=2)

# Event loop for GUI
root.mainloop()
