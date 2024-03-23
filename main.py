import json
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    # pyperclip.paste(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name =website_entry.get()
    password_name = password_entry.get()
    email_name = email_entry.get()
    new_data = {
        website_name : {
            "email":email_name,
            "password":password_name
        }
    }
    if website_name == "" or password_name == "" or email_name == "":
            messagebox.showinfo(title="Failed to Save", message="Ensure your fields are field .")

    else:
        is_ok = messagebox.askokcancel(title="Please Confirm !!", message=f"Please confirm you credentials\n"
                                                                          f" Website :{website_name}\n "
                                                                          f"Email {email_name} \n "
                                                                          f"Password : {password_name}\n"
                                                                          f"Are you sure you want to save this ?")

        if is_ok:
                try:
                    with open("data.json", mode="r") as file:
                        data_json = json.load(file)

                except FileNotFoundError:
                    with open("data.json", mode="w") as file:
                        json.dump(new_data, file, indent=4)
                    print("file not found, but we created it")

                else:
                    if website_name in data_json:
                        messagebox.showinfo(title="Hey Buddy !!",
                                            message=f"There is an existing credentials of {website_name} \n"
                                                    f"Search to find more .")
                    else:
                        data_json.update(new_data)
                        with open("data.json", mode="w") as file:
                            json.dump(data_json, file, indent=4)
                finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------__----------- #
def data_search():
#     get data that has been wriiten ,
     website_name = website_entry.get()
#     load data,
     with open ("data.json", mode="r")  as file:
         data = json.load(file)

     try:
         search = data[website_name]
     except KeyError:
         messagebox.showinfo(title=f"{website_name} credentials", message=f"There is no credentials for {website_name} at the moment")
     else:
         search_email = search["password"]
         messagebox.showinfo(title=f"{website_name} credentials", message=f"This are your credentials..\n"
                                                     f"Website :{website_name}\n "
                                                     f"Email :{search_email}")



window = Tk()
window.title("Password Manager")
window.config(padx=70,pady=50)

# canvas creating
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=2,row=1)

label_website = Label(text="Website")
label_website.grid(column=1 ,row=2)

website_entry = Entry()
website_entry.focus()
website_entry.grid(column=2, row=2, sticky = W )

website_search = Button(text="SEARCH" ,bg="blue",command= data_search)
website_search.grid(column= 3,row =2)

label_email = Label(text="Email/Username")
label_email.grid(column=1 ,row=3)

email_entry = Entry(width=35)
email_entry.insert(0,"marshamark@gmail.com")
email_entry.grid(column =2,row =3,columnspan =2,sticky = W )

label_password = Label(text="Password")
label_password.grid(column=1 ,row=4 )

password_entry = Entry(width=21)
password_entry.grid(column =2, row =4,sticky = W)

generate_password_button = Button(text="Generate Password",command = generate_password)
generate_password_button.grid(column = 3, row =4,sticky = W)

# Buttons
button_Add = Button(text="Add" ,width= 30, command=save)
button_Add.grid(column = 2, row = 5, columnspan =2)


window.mainloop()