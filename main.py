import requests
import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create and configure labels and entry fields
city_label = tk.Label(window, text="City: ", padx=100, pady=10)
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack(pady=10)

# Create a button to fetch weather data
fetch_button = tk.Button(window, text="Fetch Weather")
fetch_button.pack()

# Create a label to display weather information
weather_label =  tk.Label(window, text="", pady=10)
weather_label.pack()

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    # Add your API key here
    api_key = "fae3da343e536b353c92904586ee1eb6"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"temperature: {temperature}°C\n Weather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable a fetch weather data")

fetch_button.config(command=fetch_weather)


window.mainloop()
