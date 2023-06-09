from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    if pass_entry.get() != "":
        pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD -------------------------------#
def save():
    if len(email_entry.get()) == 0 or len(pass_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showwarning(title="Opps", message="Please don't leave any field empty.")
    else:
        want_to_save = messagebox.askyesno(title=web_entry.get(), message=f"These are the details entered:\n "
                                                                          f"Email:{email_entry.get()}\n "
                                                                          f"Password:{pass_entry.get()} "
                                                                          f"Is it ok to save?")
        new_data = {
            web_entry.get().title(): {
                "email": email_entry.get(),
                "password": pass_entry.get(),
            }
        }
        if want_to_save:
            try:
                with open("password_manager.json", mode="r") as file:
                    # load data
                    data = json.load(file)
                    # update data
                    data.update(new_data)
            except FileNotFoundError:
                with open("password_manager.json", mode="w") as file:
                    json.dump(new_data, file)
                    file.close()
            else:
                with open("password_manager.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                    file.close()
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- Find PASSWORD -------------------------------#
def find_pass():
    if len(web_entry.get()) == 0:
        messagebox.showwarning(title="Opps", message="Please don't leave website field field empty.")
    else:
        try:
            with open("password_manager.json", mode="r") as file:
                # load data
                data = json.load(file)
                email = data[web_entry.get().title()]["email"]
                password = data[web_entry.get().title()]["password"]
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file found")
        except KeyError as key:
            messagebox.showwarning(title="Error", message=f"No Records of {key} account was found")
        else:
            messagebox.showinfo(title=web_entry.get().title(), message=f"Email: {email}\nPassword: {password}")
        finally:
            web_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")
pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

# buttons
pass_button = Button(text="Generate Password", command=generate_pass)
pass_button.grid(row=3, column=2)
search_button = Button(text="Search", width=15, command=find_pass)
search_button.grid(row=1, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
