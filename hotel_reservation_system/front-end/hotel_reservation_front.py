import tkinter as tk
from tkinter import Toplevel
import tkinter.messagebox as messagebox
import requests
import tkinter as tk

import tkinter as tk
from tkinter import ttk
import requests

# Set the base URL for the API
base_url = 'http://127.0.0.1:8000/api/user'

# Set the URL for the register endpoint
register_url = base_url + '/register/'
login_url = base_url + '/login/'

def register():
    # Get the user's registration information from the form
    username = username_field.get()
    password = password_field.get()
    email = email_field.get()

    # Set the user's credentials
    user_credentials = {
        'username': username,
        'password': password,
        'email': email
    }

    # Send a POST request to the register endpoint
    response = requests.post(register_url, json=user_credentials)

    # Check the response status code
    if response.status_code == 201:
        # The user was registered successfully
        messagebox.showinfo('Registration Successful', 'User registered successfully, now you able to Log In')
    else:
        # There was an error with the request
        messagebox.showerror('Error', 'An error occurred: ' + response.text)

root = tk.Tk()
root.title("Hotel Reservation System")
root.geometry('750x350')

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Create a frame for the login tab
login_frame = tk.Frame(notebook)

# Create labels for the username and password fields
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)

# Create the username and password fields
username_field = tk.Entry(login_frame, width=25)
username_field.grid(row=0, column=1)

password_field = tk.Entry(login_frame, width=25, show="*")
password_field.grid(row=1, column=1)

# Create a frame to hold the buttons
button_frame = tk.Frame(login_frame)
button_frame.grid(row=2, column=0, columnspan=2)

# Create the Log In and Register Now buttons
log_in_button = tk.Button(button_frame, text="Log In", width=25)
log_in_button.grid(row=0, column=0)

# Add the login frame to the notebook
notebook.add(login_frame, text="Log In")

# Create a frame for the registration tab
register_frame = tk.Frame()

# Create labels for the username, password, and email fields
username_label = tk.Label(register_frame, text="Username:")
username_label.grid(row=0, column=0)

password_label = tk.Label(register_frame, text="Password:")
password_label.grid(row=1, column=0)

email_label = tk.Label(register_frame, text="Email:")
email_label.grid(row=2, column=0)

# Create the username, password, and email fields
username_field = tk.Entry(register_frame, width=25)
username_field.grid(row=0, column=1)

password_field = tk.Entry(register_frame, width=25, show="*")
password_field.grid(row=1, column=1)

email_field = tk.Entry(register_frame, width=25)
email_field.grid(row=2, column=1)

# Create a submit button
submit_button = tk.Button(register_frame, text="Submit", command=register)
submit_button.grid(row=3, column=1)

# Add the registration frame to the notebook
notebook.add(register_frame, text="Register")

# Place the notebook in the window
notebook.pack()

root.mainloop()





# # Create a Tkinter window
# window = tk.Tk()

# window.geometry('750x350')

# # Set the window title
# window.title('Registration Form')

# # Create text entry fields for the username, password, and email
# username_field = tk.Entry(window)
# password_field = tk.Entry(window, show='*')
# email_field = tk.Entry(window)

# # Set the placeholder text for the fields
# username_field.insert(0, 'Username')
# password_field.insert(0, 'Password')
# email_field.insert(0, 'Email')

# # Place the fields in the window
# username_field.grid(row=0, column=0)
# password_field.grid(row=1, column=0)
# email_field.grid(row=2, column=0)

# # Create a submit button
# submit_button = tk.Button(window, text='Register')
# submit_button1 = tk.Button(window, text='Now Log In')
# # Place the submit button in the window
# submit_button.grid(row=3, column=0)
# submit_button1.grid(row=3, column=1)

# # Set the base URL for the API
# base_url = 'http://127.0.0.1:8000/api/user'

# # Set the URL for the register endpoint
# register_url = base_url + '/register/'
# login_url = base_url + '/login/'

# def submit_form():
#     # Get the user's registration information from the form
#     username = username_field.get()
#     password = password_field.get()
#     email = email_field.get()

#     # Set the user's credentials
#     user_credentials = {
#         'username': username,
#         'password': password,
#         'email': email
#     }

#     # Send a POST request to the register endpoint
#     response = requests.post(register_url, json=user_credentials)

#     # Check the response status code
#     if response.status_code == 201:
#         # The user was registered successfully
#         messagebox.showinfo('Registration Successful', 'User registered successfully')
#     else:
#         # There was an error with the request
#         messagebox.showerror('Error', 'An error occurred: ' + response.text)


# # Set the submit button's click event to call the submit_form function
# submit_button['command'] = submit_form

# # Create a function to open the login window
# def open_login_window():
#     # Create a new Tkinter window
#     login_window = tk.Toplevel(window)

#     # Set the window title
#     login_window.title('Log In')

#     # Create text entry fields for the username and password
#     username_field = tk.Entry(login_window)
#     password_field = tk.Entry(login_window, show='*')

#     # Set the placeholder text for the fields
#     username_field.insert(0, 'Username')
#     password_field.insert(0, 'Password')

#     # Place the fields in the window
#     username_field.grid(row=0, column=0)
#     password_field.grid(row=1, column=0)

#     # Create a submit button
#     submit_button = tk.Button(login_window, text='Log In')

#     # Place the submit button in the window
#     submit_button.grid(row=2, column=0)

# # Set the submit button1's click event to call the open_login_window function
# submit_button1['command'] = open_login_window


# # Run the Tkinter event loop
# window.mainloop()
