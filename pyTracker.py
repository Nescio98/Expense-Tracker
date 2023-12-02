from customtkinter import *
from PIL import Image
import tkinter

app = CTk()
app.title("pyTracker")

width = "1600"
height = "900"
set_default_color_theme("dark-blue")
set_appearance_mode("dark")
app.geometry(width + "x" + height)
app.resizable(0, 0)

colours = { "light-blue": "#39ace7", "dark-blue": "#0784b5", "background":"#414c50", "white": "#fff"}



######################################################## MENU ########################################################
def show_page(page):
    page.pack(side="left", fill="both", expand=True)
    pages_to_hide = [p for p in [dashboard_page, transactions_page, categories_page, add_transaction_page, settings_page] if p != page]
    for p in pages_to_hide:
        p.pack_forget()

sidebar_frame = CTkFrame(master=app, fg_color="#0784b5", width=300, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("img/financial-profit.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

frame_width = int(width) - sidebar_frame.cget("width")
frame_height = int(height) - sidebar_frame.cget("height")

# Dashboard
dashboard_img_data = Image.open("img/dashboard_icon.png")
dashboard_img = CTkImage(dark_image=dashboard_img_data, light_image=dashboard_img_data,
                        size=(sidebar_frame.cget("width") * 0.8 * 0.15, sidebar_frame.cget("width") * 0.8 * 0.15))
dashboard_page = CTkFrame(master=app, width=int(width) - sidebar_frame.cget("width"), height=int(height),
                          corner_radius=0)
CTkButton(master=sidebar_frame, image=dashboard_img, text="Dashboard", fg_color="transparent",
          font=("Arial Bold", 30), hover_color="#39ace7", anchor="w", width=sidebar_frame.cget("width") * 0.8,
          height=sidebar_frame.cget("height") * 0.10, command=lambda: show_page(dashboard_page)).pack(anchor="center",
                                                                                                    ipady=5,
                                                                                                    pady=(60, 0))

# Transactions
transactions_img_data = Image.open("img/transactions_icon.png")
transactions_img = CTkImage(dark_image=transactions_img_data, light_image=transactions_img_data,
                           size=(sidebar_frame.cget("width") * 0.8 * 0.15, sidebar_frame.cget("width") * 0.8 * 0.15))
transactions_page = CTkFrame(master=app, width=int(width) - sidebar_frame.cget("width"), height=int(height),
                             corner_radius=0)
CTkButton(master=sidebar_frame, image=transactions_img, text="Transactions", fg_color="transparent",
          font=("Arial Bold", 30), hover_color="#39ace7", anchor="w", width=sidebar_frame.cget("width") * 0.8,
          height=sidebar_frame.cget("height") * 0.10, command=lambda: show_page(transactions_page)).pack(anchor="center",
                                                                                                          ipady=5,
                                                                                                          pady=(16, 0))                                                                                                        

# Categories
categories_img_data = Image.open("img/categories_icon.png")
categories_img = CTkImage(dark_image=categories_img_data, light_image=categories_img_data,
                          size=(sidebar_frame.cget("width") * 0.8 * 0.15, sidebar_frame.cget("width") * 0.8 * 0.15))
categories_page = CTkFrame(master=app, width=int(width) - sidebar_frame.cget("width"), height=int(height),
                           corner_radius=0)
CTkButton(master=sidebar_frame, image=categories_img, text="Categories", fg_color="transparent",
          font=("Arial Bold", 30), hover_color="#39ace7", anchor="w", width=sidebar_frame.cget("width") * 0.8,
          height=sidebar_frame.cget("height") * 0.10, command=lambda: show_page(categories_page)).pack(anchor="center",
                                                                                                         ipady=5,
                                                                                                         pady=(16, 0))

# Add Transaction
add_img_data = Image.open("img/add_icon.png")
add_img = CTkImage(dark_image=add_img_data, light_image=add_img_data,
                   size=(sidebar_frame.cget("width") * 0.8 * 0.15, sidebar_frame.cget("width") * 0.8 * 0.15))
add_transaction_page = CTkFrame(master=app, width=int(width) - sidebar_frame.cget("width"), height=int(height),
                                corner_radius=0)
CTkButton(master=sidebar_frame, image=add_img, text="Add Transaction", fg_color="#414c50",
          font=("Arial Bold", 30), hover_color="#39ace7", anchor="w", width=sidebar_frame.cget("width") * 0.8,
          height=sidebar_frame.cget("height") * 0.10, command=lambda: show_page(add_transaction_page)).pack(anchor="center",
                                                                                                               ipady=5,
                                                                                                               pady=(120, 0))
                                                                                                   
# Settings
settings_img_data = Image.open("img/settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data,
                        size=(sidebar_frame.cget("width") * 0.8 * 0.15, sidebar_frame.cget("width") * 0.8 * 0.15))
settings_page = CTkFrame(master=app, width=int(width) - sidebar_frame.cget("width"), height=int(height),
                         corner_radius=0)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent",
          font=("Arial Bold", 30), hover_color="#39ace7", anchor="w", width=sidebar_frame.cget("width") * 0.8,
          height=sidebar_frame.cget("height") * 0.10, command=lambda: show_page(settings_page)).pack(anchor="center",
                                                                                                      ipady=5,
                                                                                                      pady=(180, 0))

#############################################Add Transaction Page#############################################
 
# Function to handle the add transaction button click
def add_transaction():
    # Retrieve values from the form
    amount = amount_entry.get()
    category = category_combobox.get()
    date = date_entry.get_date()
    note = note_text.get("1.0", "end-1c")  # Retrieve text from the Text widget

    # Print the values (you can replace this with your logic to save the transaction)
    print("Amount:", amount)
    print("Category:", category)
    print("Date:", date)
    print("Note:", note)

def clear_form():
    amount_entry.delete(0, "end")
    category_combobox.set("")
    date_entry.set_date(datetime.datetime.now())
    note_text.delete("1.0", "end")

CTkLabel(master=add_transaction_page, text="Add Transaction", font=("Arial Black", 40), text_color=colours["dark-blue"]).pack(anchor="nw", pady=(29,0), padx=27)

grid = CTkFrame(master=add_transaction_page, fg_color="transparent")
grid.pack(fill="both", padx=27, pady=(31,0))

CTkLabel(master=grid, text="Account", font=("Arial Bold", 27), text_color=colours["dark-blue"], justify="left").grid(row=0, column=0, sticky="w")
accounts_list = ["Revolut", "BBVA", "Fineco"]  # Replace with your actual category list
CTkComboBox(master=grid, values=accounts_list, width=frame_width/2 - 65, dropdown_font=("Arial Bold", 27), font=("Arial Bold", 27)).grid(row=1, column=0, ipady=16)


CTkLabel(master=grid, text="Category", font=("Arial Bold", 27), text_color=colours["dark-blue"], justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
categories_list = ["Groceries", "Fuel", "Transports"]  # Replace with your actual category list
CTkComboBox(master=grid, values=categories_list, width=frame_width/2 - 65, dropdown_font=("Arial Bold", 27), font=("Arial Bold", 27)).grid(row=1, column=1, ipady=16, padx=(24,0))

CTkLabel(master=grid, text="Transaction Type", font=("Arial Bold", 27), text_color=colours["dark-blue"], justify="left").grid(row=2, column=0, sticky="w", pady=(38, 0))
status_var = tkinter.IntVar(value=0)
CTkRadioButton(master=grid, variable=status_var, value=0, text="Income", font=("Arial Bold", 24), text_color="#ccc8c8", fg_color="#ccc8c8", border_color="#ccc8c8", hover_color=colours["dark-blue"]).grid(row=3, column=0, sticky="w",)
CTkRadioButton(master=grid, variable=status_var, value=1,text="Expense", font=("Arial Bold", 24), text_color="#ccc8c8", fg_color="#ccc8c8", border_color="#ccc8c8", hover_color=colours["dark-blue"]).grid(row=4, column=0, sticky="w",)

CTkLabel(master=grid, text="Date", font=("Arial Bold", 27), text_color=colours["dark-blue"], justify="left").grid(row=5, column=0, sticky="w", pady=(42, 0))
date_frame = CTkEntry(master=grid, fg_color="transparent", placeholder_text="Date Format: DD-MM-YYYY", width=frame_width/2 - 65, font=("Arial Bold", 27), border_width=2)
date_frame.grid(row=6, column=0, pady=(21,0), sticky="w")

CTkLabel(master=grid, text="Amount", font=("Arial Bold", 27), text_color=colours["dark-blue"], justify="left").grid(row=2, column=1, sticky="w", pady=(38, 0),padx=(25,0))
CTkEntry(master=grid, fg_color="transparent", placeholder_text="Amount number", width=frame_width/2 - 65, font=("Arial Bold", 27), border_width=2).grid(row=3, column=1, ipady=16, padx=(24,0), sticky="w")

CTkLabel(master=grid, text="Memo", font=("Arial Bold", 27), text_color=colours["dark-blue"], justify="left").grid(row=4, column=1, sticky="w", pady=(38, 0),padx=(25,0))
CTkEntry(master=grid, fg_color="transparent", placeholder_text="Memo", width=frame_width/2 - 65, font=("Arial Bold", 27), border_width=2).grid(row=5, column=1, ipady=16, padx=(24,0), sticky="w")


'''
#### da cancellare
# Create widgets for the form
CTkLabel(master=add_transaction_page, text="Amount:").pack(pady=(20, 5))
amount_entry = CTkEntry(master=add_transaction_page, width=20)
amount_entry.pack(pady=5)

CTkLabel(master=add_transaction_page, text="Category:").pack(pady=(20, 5))
categories_list = ["Category 1", "Category 2", "Category 3"]  # Replace with your actual category list
category_combobox = CTkComboBox(master=add_transaction_page, values=categories_list)
category_combobox.pack(pady=5)


CTkLabel(master=add_transaction_page, text="Date:").pack(pady=(20, 5))
date_entry = CTkEntry(master=add_transaction_page, width=12)
date_entry.pack(pady=5)

CTkLabel(master=add_transaction_page, text="Note:").pack(pady=(20, 5))
note_text = CTkEntry(master=add_transaction_page, height=5, width=40)
note_text.pack(pady=5)
'''

# Button to add transaction
CTkButton(master=grid, text="Clear form", fg_color=colours["light-blue"], text_color="#ccc8c8", corner_radius=10,
          font=("Arial Bold", 47), hover_color=colours["dark-blue"],width=frame_width/2 - 65, command=clear_form).grid(row=7, column=0, pady=(42, 0))  

CTkButton(master=grid, text="Submit", fg_color=colours["light-blue"], text_color="#ccc8c8", corner_radius=10,
          font=("Arial Bold", 47), hover_color=colours["dark-blue"],width=frame_width/2 - 65, command=add_transaction).grid(row=7, column=1, pady=(42, 0))                                                                                                             





# Initially, display the dashboard page
show_page(dashboard_page)

app.mainloop()
