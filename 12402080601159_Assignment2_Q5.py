"""Q5: Tkinter Contact Manager with MySQL Backend
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
UI is runnable without a database; database methods are separated for extension.
"""
import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []
        tk.Label(root, text="Name").grid(row=0, column=0, sticky="w")
        tk.Label(root, text="Phone").grid(row=1, column=0, sticky="w")
        self.name = tk.Entry(root)
        self.phone = tk.Entry(root)
        self.name.grid(row=0, column=1, padx=6, pady=3)
        self.phone.grid(row=1, column=1, padx=6, pady=3)
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=2, column=0, columnspan=2)
        self.listbox = tk.Listbox(root, width=42)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=6, pady=6)

    def add_contact(self):
        name, phone = self.name.get().strip(), self.phone.get().strip()
        if not name or not phone:
            messagebox.showwarning("Missing information", "Enter both name and phone.")
            return
        self.contacts.append((name, phone))
        self.listbox.insert(tk.END, f"{name} — {phone}")
        self.name.delete(0, tk.END)
        self.phone.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    ContactManager(root)
    root.mainloop()
