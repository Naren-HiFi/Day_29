from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #

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
