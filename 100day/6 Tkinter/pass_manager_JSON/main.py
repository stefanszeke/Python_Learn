import random
import tkinter as tk
from tkinter import messagebox
import json
window = tk.Tk()

# import piperclip;
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    for _ in range(0, 11):
        password_entry.insert("end", random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"))
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(password_entry.get())
    r.update()
    r.destroy()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def is_file_valid():
    if len(web_site_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!")
        return False
    return True


def is_it_ok_to_save():
    yes_no = messagebox.askokcancel(title=web_site_entry.get(), message=f"These are the details entered: \nEmail: {
        email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")
    if not yes_no:
        return False
    return True


def save_to_file():

    # check
    if not is_file_valid():
        return
    if not is_it_ok_to_save():
        return

    # model data
    new_entry = {
        web_site_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    # read
    with open("data.json", "r") as json_file:
        try:
            data = json.load(json_file)
            data.update(new_entry)
        except:
            data = new_entry

    # write
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        web_site_entry.delete(0, "end")
        password_entry.delete(0, "end")
        print("writin")
# ----------------------------- Search -------------------------------- #
def search_website():
    if(web_site_entry.get() == ""):
        messagebox.showwarning(title="Empty field", message="Please enter a website name!")
        return
    
    with open("data.json", "r") as json_file:
        try:
            data = json.load(json_file)
            email_entry.delete(0, "end")
            email_entry.insert(0, data[web_site_entry.get()]["email"])
            password_entry.delete(0, "end")
            password_entry.insert(0, data[web_site_entry.get()]["password"])
        except KeyError:
            messagebox.showwarning(title="Not Found", message="No data found for the website!")
            return
        except:
            messagebox.showwarning(title="Error", message="Something went wrong!")
            return
        

# ---------------------------- UI SETUP ------------------------------- #


window.title("Password Manager")
window.config(
    padx=20,
    pady=20
)


canvas = tk.Canvas(width=200, height=200)

logo_img = tk.PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# row 1 website
web_site_lb = tk.Label(text="Website:")
web_site_entry = tk.Entry(width=33)
search_button = tk.Button(text="Search", width=15)

web_site_lb.grid(row=1, column=0)
web_site_entry.grid(row=1, column=1, sticky="W")
search_button.grid(row=1, column=2, sticky="W")
# row 2 email
email_lb = tk.Label(text="Email/Username:")
email_entry = tk.Entry(width=52)

email_lb.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

# row 3 password
password_lb = tk.Label(text="Password:")
password_entry = tk.Entry(width=33)
generate_password_button = tk.Button(text="Generate Password", width=15)

password_entry.grid(row=3, column=1, sticky="W")
generate_password_button.grid(row=3, column=2, sticky="W")

password_lb.grid(row=3, column=0)

# row 4 add button
add_button = tk.Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")


######
web_site_entry.focus()
email_entry.insert(0, "name@gmail.com")
add_button.config(command=save_to_file)
generate_password_button.config(command=pass_generator)
search_button.config(command=search_website)

window.mainloop()
