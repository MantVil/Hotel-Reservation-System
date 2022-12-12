import tkinter as tk
from tkinter import Toplevel
import tkinter.messagebox as messagebox
import requests
import tkinter as tk
from tkinter import ttk

base_url = 'http://127.0.0.1:8000/api/user'

register_url = base_url + '/register/'
login_url = base_url + '/login/'

def register():
    username = username_field.get()
    password = password_field.get()
    email = email_field.get()

    user_credentials = {
        'username': username,
        'password': password,
        'email': email
    }

    response = requests.post(register_url, json=user_credentials)
    if response.status_code == 201:
        messagebox.showinfo('Registration Successful', 'User registered successfully, now you able to Log In')
    else:
        messagebox.showerror('Error', 'An error occurred: ' + response.text)

def login():
    username = username_field.get()
    password = password_field.get()

    user_credentials = {
        'username': username,
        'password': password
    }

    response = requests.post(login_url, json=user_credentials)
    if response.status_code == 200:
        token = response.json().get('token')
    else:
        messagebox.showerror('Error', 'Incorrect username or password')


root = tk.Tk()
root.title("Hotel Reservation System")
root.geometry('750x350')

notebook = ttk.Notebook(root)

login_frame = tk.Frame(notebook)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)

username_field = tk.Entry(login_frame, width=25)
username_field.grid(row=0, column=1)

password_field = tk.Entry(login_frame, width=25, show="*")
password_field.grid(row=1, column=1)

button_frame = tk.Frame(login_frame)
button_frame.grid(row=2, column=0, columnspan=2)

log_in_button = tk.Button(button_frame, text="Log In", width=25, command=login)
log_in_button.grid(row=0, column=0)

notebook.add(login_frame, text="Log In")

register_frame = tk.Frame()

username_label = tk.Label(register_frame, text="Username:")
username_label.grid(row=0, column=0)

password_label = tk.Label(register_frame, text="Password:")
password_label.grid(row=1, column=0)

email_label = tk.Label(register_frame, text="Email:")
email_label.grid(row=2, column=0)

username_field = tk.Entry(register_frame, width=25)
username_field.grid(row=0, column=1)

password_field = tk.Entry(register_frame, width=25, show="*")
password_field.grid(row=1, column=1)

email_field = tk.Entry(register_frame, width=25)
email_field.grid(row=2, column=1)

submit_button = tk.Button(register_frame, text="Submit", command=register)
submit_button.grid(row=3, column=1)

notebook.add(register_frame, text="Register")
notebook.pack()

root.mainloop()


