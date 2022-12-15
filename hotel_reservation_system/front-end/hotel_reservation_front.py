
import tkinter as tk
import requests

root = tk.Tk()

hotels_label = tk.Label(root, text="List of hotels:")
hotels_label.pack()

hotels_listbox = tk.Listbox(root)
hotels_listbox.pack()

def refresh_hotels_list():
    response = requests.get('http://127.0.0.1:8000/api/hotels/')
    if response.status_code == 200:  
        hotels_listbox.delete(0, tk.END)
        hotels = response.json()
        for hotel in hotels:
            hotels_listbox.insert(tk.END, hotel['name'])

def add_hotel():
    
    hotel_name = hotel_name_entry.get()
    hotel_address = hotel_address_entry.get()
    response = requests.post('http://127.0.0.1:8000/api/hotels/', json={'name': hotel_name, 'address': hotel_address})
    if response.status_code == 201:
        
        refresh_hotels_list()

hotel_name_label = tk.Label(root, text="Hotel name:")
hotel_name_label.pack()

hotel_name_entry = tk.Entry(root)
hotel_name_entry.pack()

hotel_address_label = tk.Label(root, text="Hotel address:")
hotel_address_label.pack()

hotel_address_entry = tk.Entry(root)
hotel_address_entry.pack()

add_hotel_button = tk.Button(root, text="Add hotel", command=add_hotel)
add_hotel_button.pack()

refresh_hotels_list()


root.mainloop()