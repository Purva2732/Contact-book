import tkinter as tk
from tkinter import StringVar, messagebox
import csv
import os

# Create the main window 
window = tk.Tk()
window.geometry("500x550")
window.title("My Contact Book")

# Variables to store user input
name = StringVar()
phone = StringVar()

# Label for title
title_label = tk.Label(window, text="Enter contact details", font=('arial', 15))
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Labels and entry widgets for name, phone, and address
tk.Label(window, text="Full name", bg='grey').grid(row=1, column=0, pady=10)
name_entry = tk.Entry(window, textvariable=name)
name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Mobile no.", bg="grey").grid(row=2, column=0, padx=10, pady=10)
phone_entry = tk.Entry(window, textvariable=phone)
phone_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text="Address", bg="grey").grid(row=3, column=0, padx=10, pady=10)
address_text = tk.Text(window, width=20, height=5)
address_text.grid(row=3, column=1, padx=10, pady=10)

# Text widget to display search results
view_text = tk.Text(window, width=40, height=5)
view_text.grid(row=6, column=1, padx=10, pady=10)

def get_data():
    """Function to save user input to CSV file."""
    name_data = name.get()
    phone_data = phone.get()
    address_data = address_text.get("1.0", tk.END).strip()
    
    # Check if any field is empty
    if not name_data or not phone_data or not address_data:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    # Ensure file exists or create it
    file_exists = os.path.isfile("./users.csv")
    with open("./users.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)
        if not file_exists:
            csv_writer.writerow(["Full name", "Mobile no.", "Address"])  # Add header if file is newly created
        csv_writer.writerow([name_data, phone_data, address_data])
    
    # Clear the entries after saving
    name.set('')
    phone.set('')
    address_text.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Data saved successfully!")

def search_data():
    """Function to search for data in CSV file and display in view widget."""
    search_term = entry_search.get().strip().lower()
    view_text.delete("1.0", tk.END)  # Clear previous search results
    
    file_exists = os.path.isfile("./users.csv")
    if not file_exists: 
        messagebox.showerror("Error", "No data found. Please save data first.")
        return
    
    with open("./users.csv", "r") as file:
        csv_reader = csv.reader(file)
        found = False
        
        header = next(csv_reader)  # Skip header row
        for row in csv_reader:
            if search_term in [elem.lower() for elem in row]:
                view_text.insert(tk.END, f"{', '.join(row)}\n")
                found = True
        
        if not found:
            view_text.insert(tk.END, "No matching records found.")

# Buttons and search entry
tk.Button(window, text="Save", command=get_data).grid(row=4, column=0, padx=20, pady=20)
tk.Button(window, text="Search", command=search_data).grid(row=5, column=0, padx=20, pady=20)

entry_search = tk.Entry(window)
entry_search.grid(row=5, column=1, padx=20, pady=20)

tk.Button(window, text="Delete").grid(row=7, column=0, padx=20, pady=20)
tk.Button(window, text="Update").grid(row=7, column=1, padx=20, pady=20)

# Start the Tkinter event loop
window.mainloop()
