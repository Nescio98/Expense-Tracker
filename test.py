from customtkinter import *
from PIL import Image

app = CTk()
app.title("pyTracker")

width = "1600"
height = "900"
set_default_color_theme("dark-blue")
set_appearance_mode("dark")
app.geometry(width + "x" + height)
app.resizable(0, 0)

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
                                corner_radius=0, fg_color="#fff")
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

# Initially, display the dashboard page
show_page(dashboard_page)

app.mainloop()
