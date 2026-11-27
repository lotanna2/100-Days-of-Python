from tkinter import *
from tkinter import messagebox # not a class or contstant, just a built-in module for message boxes
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)] 
    )

    random.shuffle(password_list)

    password = "".join(password_list)
    #for char in password_list:
    #  password += char

    input_password.delete(0, END) # Clear the password input field before inserting the new password
    input_password.insert(0, password) # Insert the generated password into the password input field
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    password_data = {
        "website": website,
        "email": email,
        "password": password
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?") # returns a boolean value (True if OK is clicked, False if Cancel is clicked)

        if is_ok:
            with open("data.txt", "a") as file: # creates a file object for appending the data
                file.write(f"{password_data}\n")
                input_website.delete(0, END) # Clear the website input field after saving
                input_email.delete(0, END)
                input_password.delete(0, END)

      
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)


# image
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)


# config does not work with Entry widgets for padding, use grid options instead

# website and input fields Entries
website_label = Label(text="Website:")
website_label.config(padx=5, pady=5)
website_label.grid(row=1, column=0)
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
input_website.focus() # Set focus to the website input field on startup so the cursor is placed there immediately 


# email and input fields Entries
email_label = Label(text="Email/Username:")
email_label.config(padx=5, pady=5)
email_label.grid(row=2, column=0)
input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
input_email.insert(0, "lotaonye3@gmail.com") # Pre-fill the email input field with a default value

#password and input fields Entries
password_label = Label(text="Password:")
password_label.config(padx=5, pady=5)
password_label.grid(row=3, column=0)
input_password = Entry(width=35)
input_password.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# add button to generate password
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.config(padx=2, pady=2)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
    



window.mainloop()