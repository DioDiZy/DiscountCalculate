import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        quantity = float(entry_quantity.get())

        discount_amount = price * (discount / 100)
        final_price = (price - discount_amount) * quantity

        label_result.config(text=f"Final Price: Rp {final_price:,}")
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")

box = tk.Tk()
box.title("Discount Calculator")
box.geometry("300x350")
box.resizable(False, False)
box.configure(bg="#355872")


label_Og = tk.Label(box, text="Original Price:", font=("Arial", 12), bg="#355872" , fg="white")
label_Og.pack(pady=(20, 5))

entry_price = tk.Entry(box, font=("Arial", 12))
entry_price.pack(pady=5)

label_discount = tk.Label(box, text="Discount (%):", font=("Arial", 12), bg="#355872" , fg="white")
label_discount.pack(pady=(10, 5))

entry_discount = tk.Entry(box, font=("Arial", 12))
entry_discount.pack(pady=5)

label_quantity = tk.Label(box, text="Quantity:", font=("Arial", 12), bg="#355872" , fg="white")
label_quantity.pack(pady=(10, 5))

entry_quantity = tk.Entry(box, font=("Arial", 12))
entry_quantity.pack(pady=5)

button_calculate = tk.Button(box, text="Calculate", command=calculate, font=("Arial", 12), bg="#9CD5FF"  , fg="black", borderwidth=5, )
button_calculate.pack(pady=20)

label_result = tk.Label(box, text="", font=("Arial", 12), bg="#355872" ,fg="white")
label_result.pack(pady=10)

box.mainloop()
