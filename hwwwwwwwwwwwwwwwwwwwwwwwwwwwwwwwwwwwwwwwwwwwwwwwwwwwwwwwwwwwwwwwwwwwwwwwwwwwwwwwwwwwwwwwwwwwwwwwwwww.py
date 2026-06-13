import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Length Converter")
root.geometry("300x200")

title = tk.Label(root, text="Inches to Centimeters Converter", font=("Arial", 12))
title.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=10)

root.mainloop()