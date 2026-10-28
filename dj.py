
import tkinter as tk
from tkinter import messagebox

# Login credentials
USERNAME = "admin"
PASSWORD = "9822"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Success", "Login successful!")
        welcome_label.config(text="Welcome, " + username + "!")
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password!"
        )

# Main window
root = tk.Tk()
root.title("Login Form")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#f0f2f5")

tk.Label(
    root, text="Login Form",
    font=("Arial", 20, "bold"),
    bg="#f0f2f5"
).pack(pady=20)

tk.Label(root, text="Username:", bg="#f0f2f5").pack()

username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

tk.Label(root, text="Password:", bg="#f0f2f5").pack()

password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

tk.Button(
    root, text="Login",
    command=login,
    bg="#007bff", fg="white",
    font=("Arial", 12, "bold"),
    width=15
).pack(pady=15)

welcome_label = tk.Label(root, text="", bg="#f0f2f5")
welcome_label.pack()

root.mainloop()
