import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
import json

# Set the URL for the login endpoint
login_url = 'http://127.0.0.1:8000/api-token-auth/'



def login():
    global token
    username = username_field.get()
    password = password_field.get()

    user_credentials = {
        'username': username,
        'password': password
    }
    response = requests.post(login_url, json=user_credentials)

    if response.status_code == 200:
        token = response.json()['token']
        main_window = tk.Toplevel(root)
        main_window.title("Hotel Reservation System")
        main_window.geometry('750x350')
        notebook = ttk.Notebook(main_window)
        
        hotels_frame = tk.Frame(notebook)
        
        hotels_tree = ttk.Treeview(hotels_frame, columns=('name', 'address'))
        hotels_tree.heading('#0', text="ID")
        hotels_tree.heading('name', text='Name')
        hotels_tree.heading('address', text='Address')

        def make_reservation(hotel, room_category, check_in_date, check_out_date, num_guests):
            payload = {
                'hotel': hotel,
                'room_category': room_category,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'num_guests': num_guests
            }
            response = requests.get('http://127.0.0.1:8000/api/hotel/reservations/', json=payload)
            if response.status_code == 200:
                print('Reservation successful!')
            else:
                print('Error: reservation failed')

            make_reservation_button = tk.Button(root, text="Login", command=make_reservation)
            make_reservation_button.pack(ipadx=10, ipady=10)

            make_reservation_label = tk.Label(root, text = "Rezervacija")
            make_reservation_label.pack() 


root = tk.Tk()
root.geometry("350x250")
root.title("Hotel Reservation System - Login")

username_label = tk.Label(root, text="Username")
username_label.pack(ipadx=10, ipady=10)
username_field = tk.Entry(root)
username_field.pack(ipadx=10, ipady=10)

password_label = tk.Label(root, text = "Password")
password_label.pack(ipadx=10, ipady=10)
password_field = tk.Entry(root, show="*")
password_field.pack(ipadx=10, ipady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(ipadx=10, ipady=10)

root.mainloop()

    