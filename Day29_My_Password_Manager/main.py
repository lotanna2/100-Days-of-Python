from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
input_website.focus() # Set focus to the website input field on startup


# email and input fields Entries
email_label = Label(text="Email/Username:")
email_label.config(padx=5, pady=5)
email_label.grid(row=2, column=0)
input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
input_email.insert(0, "example@example.com") # Pre-fill the email input field with a default value

#password and input fields Entries
password_label = Label(text="Password:")
password_label.config(padx=5, pady=5)
password_label.grid(row=3, column=0)
input_password = Entry(width=35)
input_password.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# add button to generate password
generate_password_button = Button(text="Generate Password")
generate_password_button.config(padx=2, pady=2)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)




window.mainloop()