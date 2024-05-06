import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate_tax():
    # User value input retrieved
    value = float(value_entry.get())

    # Calculate the assessment value & tax
    assessment_value = 0.60 * value
    property_tax = (assessment_value / 100) * 0.75 # Calculated based on assignment given numbers
    
    # Results displayed updated with calculated values
    result.set(f"Assessed Value: ${assessment_value:.2f}\nProperty Tax: ${property_tax:.2f}")

# Main window created 
root = tk.Tk()
root.title("Property Tax Calculator by Austin Kinnear")

# Variable that will hold the results
result = tk.StringVar()

# Main GUI widget panel 
value_label = tk.Label(root, text="Enter the actual property value:")
value_label.pack()
value_entry = tk.Entry(root)
value_entry.pack()

# Calculation button, calculating tax
calculate_btn = tk.Button(root, text="Calculate Tax", command=calculate_tax)
calculate_btn.pack()

# Display label of results within the GUI
results_label = tk.Label(root, textvariable=result)
results_label.pack()

root.mainloop()
