# Password Manager

A simple password manager with a graphical user interface built with tkinter in python that allows users to generate, store and retrieve passwords for different websites. 

![Screenshot (13)](https://user-images.githubusercontent.com/87391223/233421529-9f66790b-f557-4194-b639-e266b450f9fc.png)

## Features
- Generate random passwords
- Store website, email and password information
- Retrieve website, email and password information

## Getting Started
To get started with this program, simply clone the repository and run the `main.py` file. 

### Prerequisites
- Python 3.x
- tkinter
- pyperclip

### Installation
1. Clone the repository: 
   ```
   git clone https://github.com/your_username/password-manager.git
   ```
2. Install dependencies:
   ```
   pip install tkinter
   pip install pyperclip
   ```
3. Run the program:
   ```
   python main.py
   ```

## Usage
1. Generate a password: Click the `Generate Password` button to generate a password. A password will be generated and copied to the clipboard.
2. Store a password: Enter the website, email and password information in the corresponding fields and click the `Add` button to store the information.
3. Retrieve a password: Enter the website information in the `Website` field and click the `Search` button to retrieve the email and password information.

## File structure
```
├── main.py                    # Main program file
├── password_manager.json      # JSON file to store password information
└── logo.png                   # Logo image file
```

## Functions:
Generating a Random Password:
```python
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
```
Find Passwords:
```python
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
```
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
