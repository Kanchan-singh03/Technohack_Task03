import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        self.temperature_var = tk.DoubleVar()

        # Entry widget for temperature input
        self.temperature_entry = ttk.Entry(root, textvariable=self.temperature_var, width=10)
        self.temperature_entry.grid(row=0, column=0, padx=10, pady=10)

        # Combobox for selecting conversion type
        self.conversion_type_var = tk.StringVar()
        self.conversion_type_var.set("Celsius to Fahrenheit")

        self.conversion_type_combobox = ttk.Combobox(root, textvariable=self.conversion_type_var,
                                                     values=["Celsius to Fahrenheit", "Fahrenheit to Celsius",
                                                             "Celsius to Kelvin", "Kelvin to Celsius",
                                                             "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])
        self.conversion_type_combobox.grid(row=0, column=1, padx=10, pady=10)

        # Button to perform the conversion
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_temperature)
        self.convert_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Label to display the result
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_var.get())
            conversion_type = self.conversion_type_var.get()

            if conversion_type == "Celsius to Fahrenheit":
                result = celsius_to_fahrenheit(temperature)
            elif conversion_type == "Fahrenheit to Celsius":
                result = fahrenheit_to_celsius(temperature)
            elif conversion_type == "Celsius to Kelvin":
                result = celsius_to_kelvin(temperature)
            elif conversion_type == "Kelvin to Celsius":
                result = kelvin_to_celsius(temperature)
            elif conversion_type == "Fahrenheit to Kelvin":
                result = fahrenheit_to_kelvin(temperature)
            elif conversion_type == "Kelvin to Fahrenheit":
                result = kelvin_to_fahrenheit(temperature)

            self.result_label.config(text=f"Result: {result:.2f}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
