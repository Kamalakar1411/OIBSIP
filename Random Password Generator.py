import tkinter as tk
import string
import random
import pyperclip
from tkinter import messagebox

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    update_strength_indicator(password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Warning", "Generate a password before copying.")

def update_strength_indicator(password):
    strength = calculate_password_strength(password)
    strength_label.config(text=f"Strength: {strength}")

def calculate_password_strength(password):
    length = len(password)
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    digit_count = sum(1 for char in password if char.isdigit())
    special_count = length - uppercase_count - lowercase_count - digit_count

    strength = 0
    strength += min(1, length // 8)  
    strength += min(1, uppercase_count // 2) 
    strength += min(1, lowercase_count // 2)  
    strength += min(1, digit_count // 2)  
    strength += min(1, special_count // 2)  

    return int(strength * 100)

root = tk.Tk()
root.title("Password Generator")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0, sticky="W")

# Increased width from 30 to 50
password_entry = tk.Entry(root, width=40)
password_entry.grid(row=0, column=1)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=1, column=1, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=2, column=1, pady=10)

strength_label = tk.Label(root, text="Strength: 0")
strength_label.grid(row=4, column=1, columnspan=2, pady=10)

root.mainloop()
