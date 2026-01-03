import tkinter as tk
from tkinter import *
from logic import *

FILE_NAME = "contacts.csv"
pb = PhoneBook()
pb.load(FILE_NAME)
#+++++
def update_list(data=None):
    listbox.delete(0, tk.END)
    
    if data is not None:
        list_to_show = data
    else:
        list_to_show = pb.contacts
        
    for c in list_to_show:
        listbox.insert(tk.END, f"{c.name} - {c.phone}")
#+++++
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    try:
        pb.add(name, phone)
        update_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showinfo("خطا", "شماره تلفن باید عدد باشد")
#+++++
def search_contact():
    search_text = search_entry.get()
    results = pb.search(search_text)
    update_list(results)
#+++++
def delete_contact():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        full_text = listbox.get(index)

        name = full_text.split(" - ")[0]
        pb.delete(name)
        update_list()
#+++++
def exit_app():
    pb.save(FILE_NAME)
    root.destroy()

#----
root = tk.Tk()
root.title("دفترچه تلفن")
root.configure(bg='#f0f0f0')    

tk.Label(root, text="نام:", bg='#f0f0f0').pack(pady=2)
name_entry = tk.Entry(root)
name_entry.pack(pady=2)

tk.Label(root, text="تلفن:", bg='#f0f0f0').pack(pady=2)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=2)

tk.Button(root, text="افزودن مخاطب", command=add_contact, bg='#4caf50', fg='white').pack(pady=10)

tk.Label(root, text="جستجو:", bg='#f0f0f0').pack(pady=2)
search_entry = tk.Entry(root)
search_entry.pack(pady=2)
tk.Button(root, text="بگرد", command=search_contact, bg='#2196f3', fg='white').pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

tk.Button(root, text="حذف انتخاب شده", command=delete_contact, bg='#f44336', fg='white').pack(pady=5)
tk.Button(root, text="ذخیره و خروج", command=exit_app, bg='#9e9e9e', fg='white').pack(pady=10)

update_list()

root.mainloop()

#----