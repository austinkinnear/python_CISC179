import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate_tax():
    # Get the actual value entered by the user
    actual_value = float(actual_value_entry.get())
    
    # Calculate the assessment value and tax
    assessment_value = 0.60 * actual_value
    property_tax = (assessment_value / 100) * 0.75
    
    # Display the results
    result_text.set(f"Assessed Value: ${assessment_value:.2f}\nProperty Tax: ${property_tax:.2f}")

# Create the main window
root = tk.Tk()
root.title("Property Tax Calculator")

# Create a variable to hold the results
result_text = tk.StringVar()

# Create and place the entry widget for the actual property value
actual_value_label = tk.Label(root, text="Enter the actual property value:")
actual_value_label.pack()
actual_value_entry = tk.Entry(root)
actual_value_entry.pack()

# Create and place the button to calculate the tax
calculate_btn = tk.Button(root, text="Calculate Tax", command=calculate_tax)
calculate_btn.pack()

# Create and place a label to display the results
results_label = tk.Label(root, textvariable=result_text)
results_label.pack()

# Start the GUI event loop
root.mainloop()
