import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather information
def get_weather():
    city = entry_city.get()
    api_key = 'c2f8d3caca59ccbdb64ab3840a940f21'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the city was found
        if data['cod'] == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            weather_info = f'Temperature: {temp}°C\nDescription: {description.capitalize()}'
            label_result.config(text=weather_info)
        else:
            # Show an error message if the city is not found
            messagebox.showerror('Error', 'City not found')
    except Exception as e:
        # Show an error message if there was a problem with the request
        messagebox.showerror('Error', str(e))

# Create the main window
root = tk.Tk()
root.title('Weather App')

# Create and place widgets
tk.Label(root, text='Enter City:').pack(pady=10)
entry_city = tk.Entry(root)
entry_city.pack(pady=5)

tk.Button(root, text='Get Weather', command=get_weather).pack(pady=10)

label_result = tk.Label(root, text='', font=('Helvetica', 12))
label_result.pack(pady=10)

# Start the main event loop
root.mainloop()
