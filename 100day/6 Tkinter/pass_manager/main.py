import random
import tkinter as tk
from tkinter import messagebox
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


def save_to_file():
    with open("data.txt", "a") as data_file:

        if len(web_site_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
            messagebox.showwarning(
                title="Oops", message="Please don't leave any fields empty!")
            return

        yes_no = messagebox.askokcancel(title=web_site_entry.get(), message=f"These are the details entered: \nEmail: {
                                        email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")

        if not yes_no:
            return

        data_file.write(f"{web_site_entry.get()} | {
                        email_entry.get()} | {password_entry.get()}\n")
        web_site_entry.delete(0, "end")
        password_entry.delete(0, "end")

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

web_site_lb = tk.Label(text="Website:")
email_lb = tk.Label(text="Email/Username:")
password_lb = tk.Label(text="Password:")

web_site_lb.grid(row=1, column=0)
email_lb.grid(row=2, column=0)
password_lb.grid(row=3, column=0)

web_site_entry = tk.Entry(width=52)
email_entry = tk.Entry(width=52)
password_entry = tk.Entry(width=33)
generate_password_button = tk.Button(text="Generate Password")
add_button = tk.Button(text="Add", width=44)

web_site_entry.grid(row=1, column=1, columnspan=2, sticky="W")
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
password_entry.grid(row=3, column=1, sticky="W")
generate_password_button.grid(row=3, column=2, sticky="W")
add_button.grid(row=4, column=1, columnspan=2, sticky="W")


######
web_site_entry.focus()
email_entry.insert(0, "name@gmail.com")
add_button.config(command=save_to_file)
generate_password_button.config(command=pass_generator)

window.mainloop()
