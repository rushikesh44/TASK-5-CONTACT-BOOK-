# Contact Book

import tkinter as tk
from tkinter import messagebox, ttk


# Contact Book Class
class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        self.contacts = []

        # Title Label
        title = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"), fg="white", bg="blue")
        title.pack(fill=tk.X)

        # Form Fields
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        form_frame = tk.Frame(root, padx=10, pady=10)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:").grid(row=0, column=0)
        tk.Entry(form_frame, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(form_frame, text="Phone:").grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0)
        tk.Entry(form_frame, textvariable=self.email_var).grid(row=2, column=1)

        tk.Label(form_frame, text="Address:").grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.address_var).grid(row=3, column=1)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Contact", bg="green", fg="white", command=self.add_contact).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=5)
        tk.Button(button_frame, text="Update Contact", bg="orange", fg="white", command=self.update_contact).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=5)
        tk.Button(button_frame, text="Delete Contact", bg="red", fg="white", command=self.delete_contact).grid(row=0,
                                                                                                               column=2,
                                                                                                               padx=5)
        tk.Button(button_frame, text="Search Contact", bg="blue", fg="white", command=self.search_contact).grid(row=0,
                                                                                                                column=3,
                                                                                                                padx=5)

        # Contact List
        self.contact_list = ttk.Treeview(root, columns=("Name", "Phone"), show='headings')
        self.contact_list.heading("Name", text="Name")
        self.contact_list.heading("Phone", text="Phone")
        self.contact_list.pack(fill=tk.BOTH, expand=True)
        self.contact_list.bind("<ButtonRelease-1>", self.select_contact)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone:
            self.contacts.append([name, phone, email, address])
            self.refresh_contact_list()
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")

    def update_contact(self):
        selected_item = self.contact_list.selection()
        if selected_item:
            index = self.contact_list.index(selected_item[0])
            self.contacts[index] = [self.name_var.get(), self.phone_var.get(), self.email_var.get(),
                                    self.address_var.get()]
            self.refresh_contact_list()
        else:
            messagebox.showerror("Error", "No contact selected!")

    def delete_contact(self):
        selected_item = self.contact_list.selection()
        if selected_item:
            index = self.contact_list.index(selected_item[0])
            del self.contacts[index]
            self.refresh_contact_list()
        else:
            messagebox.showerror("Error", "No contact selected!")

    def search_contact(self):
        search_term = self.name_var.get()
        filtered_contacts = [c for c in self.contacts if search_term.lower() in c[0].lower()]
        self.refresh_contact_list(filtered_contacts)

    def select_contact(self, event):
        selected_item = self.contact_list.selection()
        if selected_item:
            index = self.contact_list.index(selected_item[0])
            contact = self.contacts[index]
            self.name_var.set(contact[0])
            self.phone_var.set(contact[1])
            self.email_var.set(contact[2])
            self.address_var.set(contact[3])

    def refresh_contact_list(self, contacts=None):
        for row in self.contact_list.get_children():
            self.contact_list.delete(row)
        for contact in (contacts if contacts is not None else self.contacts):
            self.contact_list.insert("", tk.END, values=(contact[0], contact[1]))

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")


# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
