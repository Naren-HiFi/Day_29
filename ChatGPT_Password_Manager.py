import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def add_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Add your code here to save the data securely (e.g., in a database or encrypted file)

    messagebox.showinfo("Success", "Entry added successfully!")

# Create the main application window
root = tk.Tk()
root.title("Password Manager")

# Logo (replace 'path_to_logo.png' with the path to your logo image)
logo_image = tk.PhotoImage(file='logo.png')
logo_label = tk.Label(root, image=logo_image)
logo_label.grid(row=0, column=0, columnspan=2)

# Website label and entry
website_label = tk.Label(root, text="Website:")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(root)
website_entry.grid(row=1, column=1)

# Email/Username label and entry
email_label = tk.Label(root, text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# Add button
add_button = tk.Button(root, text="Add", command=add_entry)
add_button.grid(row=4, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
