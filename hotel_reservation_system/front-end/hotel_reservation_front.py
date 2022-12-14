import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox

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
        
        notebook.add(hotels_frame, text="Hotels")
        hotels_tree.pack()
        reservation_frame = tk.Frame(notebook)
        reservation_tree = ttk.Treeview(reservation_frame, columns =('hotel', 'room_category', 'check_in_date', 'check_out_date', 'num_guests'))
        reservation_tree.heading("#0", text="ID")
        reservation_tree.heading("hotel", text="Hotel")
        reservation_tree.heading("room_category", text="Room Category")
        reservation_tree.heading("check_in_date", text=" Check In")
        reservation_tree.heading("check_out_date", text="Check Out")
        reservation_tree.heading("num_guests", text="Number of guests")
        notebook.add(reservation_frame, text = "Make a Reservation")
        reservation_tree.pack()
        notebook.pack()
        hotels_url = 'http://127.0.0.1:8000/api/hotels/'
        reservation_url = 'http://127.0.0.1:8000/api/hotel/reservations/'
        
        response = requests.get(hotels_url, headers={'Authentication': f'Token {token}'})
        response = requests.get(hotels_url)
        if response.status_code == 200:
            hotels = response.json()

            for hotel in hotels:
                hotel_id = hotel['id']
                hotel_name = hotel['name']
                hotel_address = hotel['address']
                hotels_tree.insert('', 'end', text=hotel_id, values=(hotel_name, hotel_address))
                def on_click_hotel(event):
                    reservation_window = tk.TopLevel(main_window)
                    reservation_window.title(hotel_name)
                    hotels_tree.bind('<Button-1>', on_click_hotel)
            else:
                print("An error occurred while retrieving the list of hotels")
                print(response.status_code)
                print(response.json())
        else:
            print("An error occurred while loggin in")
            print(response.status_code)
            print(response.json())

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

    