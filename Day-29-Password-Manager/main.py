from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)
    pwd_input.insert(0, password)
    pyperclip.copy(password)

    #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get() 
    email = email_input.get()
    password = pwd_input.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                    f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open(r"Day-29-Password-Manager\data.txt", "a") as password_file:
                data = f"{website} | {email} | {password}\n"
                password_file.write(data)
            website_input.delete(0, END)
            email_input.delete(0, END)
            pwd_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"Day-29-Password-Manager\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
pwd_label = Label(text="Password: ")
pwd_label.grid(column=0, row=3)

#Entries
website_input = Entry(width=43)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=43)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "fulan@gmail.com")

pwd_input = Entry(width=25)
pwd_input.grid(column=1, row=3, ipadx=0)

#Buttons
pwd_button = Button(text="Generate Password", width=14, padx=0, command=generate_password)
pwd_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, ipadx=5)

window.mainloop()