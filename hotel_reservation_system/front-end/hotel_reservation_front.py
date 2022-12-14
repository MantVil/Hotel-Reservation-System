import tkinter as tk
import requests

# Create the root window
root = tk.Tk()

# Create a label to display the list of hotels
hotels_label = tk.Label(root, text="List of hotels:")
hotels_label.pack()

# Create a listbox to display the hotels
hotels_listbox = tk.Listbox(root)
hotels_listbox.pack()

# Define a function to refresh the list of hotels
def refresh_hotels_list():
    # Make a GET request to the /api/hotels/ endpoint to get the list of hotels
    response = requests.get('http://127.0.0.1:8000/api/hotels/')

    # Check that the request was successful
    if response.status_code == 200:
        # Clear the listbox
        hotels_listbox.delete(0, tk.END)

        # Get the list of hotels from the response data
        hotels = response.json()

        # Add each hotel to the listbox
        for hotel in hotels:
            hotels_listbox.insert(tk.END, hotel['name'])

# Define a function to add a new hotel
def add_hotel():
    # Get the hotel name and address from the user
    hotel_name = hotel_name_entry.get()
    hotel_address = hotel_address_entry.get()

    # Make a POST request to the /api/hotels/ endpoint to add the hotel
    response = requests.post('http://127.0.0.1:8000/api/hotels/', json={'name': hotel_name, 'address': hotel_address})

    # Check that the request was successful
    if response.status_code == 201:
        # Refresh the list of hotels
        refresh_hotels_list()

# Create a label for the hotel name entry field
hotel_name_label = tk.Label(root, text="Hotel name:")
hotel_name_label.pack()

# Create an entry field for the hotel name
hotel_name_entry = tk.Entry(root)
hotel_name_entry.pack()

# Create a label for the hotel address entry field
hotel_address_label = tk.Label(root, text="Hotel address:")
hotel_address_label.pack()

# Create an entry field for the hotel address
hotel_address_entry = tk.Entry(root)
hotel_address_entry.pack()

# Create a button to add the hotel
add_hotel_button = tk.Button(root, text="Add hotel", command=add_hotel)
add_hotel_button.pack()

# Refresh the list of hotels
refresh_hotels_list()

# Start the Tkinter event loop
root.mainloop()
