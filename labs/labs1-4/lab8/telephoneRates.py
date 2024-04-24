import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate_charge():
    # Get the selected rate category and minutes
    minutes = int(minutes_entry.get())
    if rate_var.get() == "Daytime":
        rate = 0.07
    elif rate_var.get() == "Evening":
        rate = 0.12
    else:
        rate = 0.05
    
    # Calculate the charge
    charge = rate * minutes
    
    # Show the charge in an info dialog
    messagebox.showinfo("Total Charge", f"The total charge for the call is ${charge:.2f}")

# Create the main window
root = tk.Tk()
root.title("Call Charge Calculator")

# Create a variable to hold the selected rate category
rate_var = tk.StringVar(value="Daytime")

# Create and place the radiobuttons for rate selection
rates = [("Daytime", "Daytime"), ("Evening", "Evening"), ("Off-Peak", "Off-Peak")]
for text, mode in rates:
    rb = tk.Radiobutton(root, text=text, variable=rate_var, value=mode)
    rb.pack(anchor=tk.W)

# Create and place the entry widget for minutes
minutes_label = tk.Label(root, text="Enter the minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

# Create and place the calculate button
calculate_btn = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_btn.pack()

# Start the GUI event loop
root.mainloop()
