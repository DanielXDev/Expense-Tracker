import tkinter as tk
from tkinter import PhotoImage
from expense_tracker import ExpenseTracker
import os
import pandas as pd


class ExpenseTrackerApp:
    def __init__(self, root, img):
        self.root = root
        self.root.geometry("400x400")  
        self.root.resizable(False, False)
        self.root.title("Expenses Tracker")
        self.expenses = []

        self.frame1 = tk.Frame(root, width=400, height=500, bg="#f7f7f7")
        self.frame2 = tk.Frame(root, width=400, height=500, bg="#f7f7f7")
        self.frame3 = tk.Frame(root, width=400, height=500, bg="#f7f7f7")
        self.bg_img = img

        self.setup_page1()
        self.frame1.grid(row=0, column=0, sticky="nsew")

    def create_canvas(self, frame):
        canvas = tk.Canvas(frame, width=400, height=500, bg="#f7f7f7", highlightthickness=0)
        canvas.create_image(200, 250, image=self.bg_img)
        canvas.grid(row=0, column=1)
        return canvas

    def add_placeholder(self, entry, text):
        # ------- Add a placeholder behavior for Entry widgets ------ #
        entry.insert(0, text)
        entry.config(fg="gray")

        def on_focus_in(event):
            if entry.get() == text:
                entry.delete(0, tk.END)
                entry.config(fg="black")

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, text)
                entry.config(fg="gray")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def setup_page1(self):
        # ------- First Page ------- #
        canvas = self.create_canvas(self.frame1)
        canvas.create_text(200, 80, text="Expenses Tracker", font=("Arial", 22, "bold"), fill="#333")
        username_entry = tk.Entry(self.frame1, bg="white", fg="black", font=("Arial", 12), relief="flat", bd=2)
        self.add_placeholder(username_entry, "Enter Username")

        submit_btn = tk.Button(self.frame1, text="Submit", font=("Arial", 12, "bold"),
                               bg="#333", fg="white", relief="flat", padx=10, pady=5,
                               command=lambda: self.show_page2(
                                   username_entry.get()) if username_entry.get() != "Enter Username" else None)

        # Placing widgets
        canvas.create_window(200, 200, window=username_entry, width=220, height=30)
        canvas.create_window(200, 250, window=submit_btn, width=100, height=35)

    def setup_page2(self, user):
        # ------- Second Page ------- #
        canvas = self.create_canvas(self.frame2)
        canvas.create_text(200, 100, text=f"Welcome, {user}!", font=("Arial", 16, "normal"), fill="#444")

        # Entries with placeholders
        category_entry = tk.Entry(self.frame2, font=("Arial", 12), relief="flat", bd=2)
        self.add_placeholder(category_entry, "Food, Bills, Clothing...")

        amount_entry = tk.Entry(self.frame2, font=("Arial", 12), relief="flat", bd=2)
        self.add_placeholder(amount_entry, "Enter amount")

        date_entry = tk.Entry(self.frame2, font=("Arial", 12), relief="flat", bd=2)
        self.add_placeholder(date_entry, "dd-mm-yyyy")

        # Buttons
        expense_submit_btn = tk.Button(self.frame2, text="Submit", font=("Arial", 12, "bold"),
                                       bg="#333", fg="white", relief="flat", padx=10, pady=5,
                                       command=lambda: self.submit_expense(user, category_entry, amount_entry,
                                                                           date_entry))

        calculate_expense_btn = tk.Button(self.frame2, text="View Expenses", font=("Arial", 12, "bold"),
                                          bg="#FF5722", fg="white", relief="flat", padx=10, pady=5,
                                          command=lambda: self.show_page3(user))

        # Placing the widgets
        canvas.create_window(200, 150, window=category_entry, width=220, height=30)
        canvas.create_window(200, 200, window=amount_entry, width=220, height=30)
        canvas.create_window(200, 250, window=date_entry, width=220, height=30)
        canvas.create_window(200, 310, window=expense_submit_btn, width=120, height=35)
        canvas.create_window(200, 360, window=calculate_expense_btn, width=120, height=35)

    def setup_page3(self, user):
        canvas = self.create_canvas(self.frame3)
        canvas.create_text(200, 50, text="Expense Summary", font=("Arial", 16, "bold"), fill="#222")

        if os.path.exists("ex.csv"):
            data = pd.read_csv("ex.csv")
            data_dict = data.groupby("Categories")["Amount"].sum().to_dict()
            data_dict["Total Spending"] = sum(data["Amount"].tolist())

            y_position = 120
            self.expenses.clear()

            for key, value in data_dict.items():
                font_style = ("Arial", 12, "bold") if key == "Total Spending" else ("Arial", 12)
                color = "#000" if key != "Total Spending" else "#D32F2F"

                cat = canvas.create_text(120, y_position, text=key, font=font_style, fill=color)
                amt = canvas.create_text(270, y_position, text=f"${value}", font=font_style, fill=color)

                self.expenses.append(cat)
                self.expenses.append(amt)
                y_position += 40

            back_btn = tk.Button(self.frame3, text="Back", font=("Arial", 12, "bold"),
                                 bg="#9E9E9E", fg="white", relief="flat", padx=10, pady=5,
                                 command=lambda: self.show_page2(user))

            canvas.create_window(200, 350, window=back_btn, width=100, height=35)
        else:
            canvas.create_text(200, 150, text="No expense data available.", font=("Arial", 12), fill="#555")

    def submit_expense(self, user, category, amount, date):
        if category.get() and amount.get() and date.get():
            ExpenseTracker(user, category.get(), amount.get(), date.get())
            category.delete(0, tk.END)
            amount.delete(0, tk.END)
            date.delete(0, tk.END)
        else:
            print("All fields are required!")

    def show_page1(self):
        self.frame1.grid(row=0, column=0, sticky="nsew")

    def show_page2(self, username):
        self.frame1.grid_forget()
        self.frame3.grid_forget()
        self.setup_page2(username)
        self.frame2.grid(row=0, column=0, sticky="nsew")

    def show_page3(self, username):
        self.frame2.grid_forget()
        self.setup_page3(username)
        self.frame3.grid(row=0, column=0, sticky="nsew")


rt = tk.Tk()
bg_img = PhotoImage(file="bg.png")
app = ExpenseTrakerApp(rt, bg_img)
rt.mainloop()
