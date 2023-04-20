<h1> Password Manager</h1>

![Screenshot (13)](https://user-images.githubusercontent.com/87391223/233421529-9f66790b-f557-4194-b639-e266b450f9fc.png)


## Introduction:

This is a password manager program written in Python using the tkinter GUI toolkit. The program allows the user to store website URLs, email addresses, and passwords for various online accounts. The user can also generate a strong, random password if they wish.


## Requirements:

    Python 3.0 or higher
    The tkinter module
    The pyperclip module
## Installation

Install Python on your computer, if you haven't already. You can download the latest version of Python from the official website: https://www.python.org/downloads/
Install the required packages by running the following command in your terminal or command prompt:

    pip install tkinter pyperclip

Download the source code from the repository and extract it to a directory of your choice.
Open the terminal or command prompt and navigate to the directory where you extracted the source code.
Run the following command to start the application:

    python password_manager.py

That's it! The Password Manager application should open and you can start using it to generate and save passwords.

## How to Use:

    Open the terminal or command prompt on your computer.
    Navigate to the directory where the program file is saved.
    Run the program by executing the command "python password_manager.py".
    Enter the details for the website, email address, and password in the corresponding entry fields.
    Click the "Generate Password" button to generate a strong, random password.
    Click the "Add" button to save the details to the password manager file.
    To view the saved passwords, open the "password_manager.txt" file located in the same directory as the program file.

## Important Note:

It is important to keep the "password_manager.txt" file secure, as it contains sensitive information. Consider encrypting the file or storing it in a secure location.

## Functions:
Generating a Random Password:
```python
def generate_pass():
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

```
Saving Passwords:
```python
def save():
    if len(email_entry.get()) == 0 or len(pass_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showwarning(title="Opps", message="Please don't leave any field empty.")
    else:
        want_to_save = messagebox.askyesno(title=web_entry.get(), message=f"These are the details entered:\n "
                                                                          f"Email:{email_entry.get()}\n "
                                                                          f"Password:{pass_entry.get()} "
                                                                          f"Is it ok to save?")
        if want_to_save:
            with open("password_manager.txt", mode="a") as file:
                file.write(f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

```

That's it! With this Password Manager, you can easily manage your passwords and get rid of remembering them.
 ## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
