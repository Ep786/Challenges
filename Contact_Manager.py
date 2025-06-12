import tkinter as tk
from tkinter import simpledialog, messagebox

contacts = []

def add_contact():
    name = simpledialog.askstring("Add", "Name?")
    email = simpledialog.askstring("Add", "Email?")
    phone = simpledialog.askstring("Add", "Phone?")
    if name and email and phone:
        contacts.append({'name': name, 'email': email, 'phone': phone})
        update_listbox()

def delete_contact():
    sel = listbox.curselection()
    if sel:
        contacts.pop(sel[0])
        update_listbox()

def edit_contact():
    sel = listbox.curselection()
    if sel:
        index = sel[0]
        contact = contacts[index]
        name = simpledialog.askstring("Edit", "Name?", initialvalue=contact['name'])
        email = simpledialog.askstring("Edit", "Email?", initialvalue=contact['email'])
        phone = simpledialog.askstring("Edit", "Phone?", initialvalue=contact['phone'])
        if name and email and phone:
            contacts[index] = {'name': name, 'email': email, 'phone': phone}
            update_listbox()

def search_contacts():
    term = simpledialog.askstring("Search", "Search?")
    listbox.delete(0, tk.END)
    for c in contacts:
        if term.lower() in c['name'].lower() or term.lower() in c['email'].lower() or term.lower() in c['phone']:
            listbox.insert(tk.END, f"{c['name']} | {c['email']} | {c['phone']}")

def update_listbox():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} | {c['email']} | {c['phone']}")

root = tk.Tk()
root.title("Contacts")

listbox = tk.Listbox(root)
listbox.pack()

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Add", command=add_contact).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Edit", command=edit_contact).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Delete", command=delete_contact).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Search", command=search_contacts).pack(side=tk.LEFT)

update_listbox()
root.mainloop()