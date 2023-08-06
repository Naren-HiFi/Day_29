from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Password Generator"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message='No data file found.')
    else:
        if website in data:
               email = data[website]["email"]
               password = data[website]["password"]
               messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title="Error", message=f'No details for {website} exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
logo_label = Label(window, image=logo_img)
logo_label.grid(row=0, column=1)

# Label
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

# Entry
website_entry = Entry(window, width=51)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Button
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2, columnspan=1)

# Label
email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

# Entry
email_entry = Entry(window, width=51)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")

# Label
password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entry
password_entry = Entry(window, width=33)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(window, text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3, columnspan=1)
add_button = Button(window, text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()
