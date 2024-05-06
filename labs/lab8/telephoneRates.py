import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    # Function to calculate all rates along with 
    minutes = int(minutes_entry.get())
    if rate_var.get() == "Daytime":
        rate = 0.07
    elif rate_var.get() == "Evening":
        rate = 0.12
    else:
        rate = 0.05
    
    charge = rate * minutes
    
    # Output of the calculation for each rate
    messagebox.showinfo("Total Charge", f"The total charge for the call is ${charge:.2f}")

# GUI display 
root = tk.Tk()
root.title("Call Charge Calculator by Austin Kinnear")

# Create a variable to hold the selected rate category
rate_var = tk.StringVar(value="Daytime")

# Create and place the radiobuttons for rate selection with descriptive text
rate_descriptions = [
    ("Daytime (6:00 a.m. through 5:59 p.m.)", "Daytime", "$0.07/min"),
    ("Evening (6:00 p.m. through 11:59 p.m.)", "Evening", "$0.12/min"),
    ("Off-Peak (midnight through 5:59 a.m.)", "Off-Peak", "$0.05/min")
]

for desc, mode, rate in rate_descriptions:
    frame = tk.Frame(root)
    frame.pack(anchor=tk.W, fill=tk.X)
    tk.Radiobutton(frame, text=f"{desc}", variable=rate_var, value=mode).pack(side=tk.LEFT)
    tk.Label(frame, text=f"{rate}").pack(side=tk.RIGHT)

# Minute input location
minutes_label = tk.Label(root, text="Enter the minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

# Calculate button 
calculate_btn = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_btn.pack()
root.mainloop()
