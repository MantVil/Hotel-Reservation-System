import tkinter as tk
import requests
from tkinter import messagebox

# Set the URL for the login endpoint
login_url = 'http://127.0.0.1:8000/api-token-auth/'

# Define the login function
def login():
    global token  # Declare the token variable as global so it can be accessed later
    username = username_field.get()  # Retrieve the value entered by the user in the username field
    password = password_field.get()  # Retrieve the value entered by the user in the password field

    user_credentials = {
        'username': username,
        'password': password
    }

    response = requests.post(login_url, json=user_credentials)
    if response.status_code == 200:
        token = response.json()['token']  # Store the token
        messagebox.showinfo('Log In Successful', 'Logged in successfully')
    else:
        messagebox.showerror('Error', 'An error occurred: ' + response.text)

# Create the main window
root = tk.Tk()
root.title("Hotel Reservation System")
root.geometry('350x150')

# Create the username and password fields
# Create the username and password fields
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0)
username_field = tk.Entry(root, width=25)
username_field.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_field = tk.Entry(root, width=25, show="*")
password_field.grid(row=1, column=1)

# Create the Log In button
login_button = tk.Button(root, text="Log In", command=login)
login_button.grid(row=2, column=1)

# Start the Tkinter event loop
root.mainloop()
