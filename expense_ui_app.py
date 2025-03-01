import tkinter as tk
from tkinter import PhotoImage
from expense_tracker import ExpenseTracker
import os
import pandas as pd

class ExpenseTrakerApp:
    def __init__(self, root, img):
        self.root = root
        self.root.geometry("400x400")
        self.expenses = []

        self.frame1= tk.Frame(root, width=400, height=400)
        self.frame2 = tk.Frame(root, width=400, height=400)
        self.frame3 = tk.Frame(root, width=400, height=400)
        self.bg_img = img


        self.setup_page1()

        self.frame1.grid(row=0, column=0, sticky="nsew")

    def create_canvas(self, frame):
        canvas = tk.Canvas(frame, width=400, height=400)
        canvas.create_image(200, 200, image=self.bg_img)
        canvas.create_text(200, 100, text="Expense Tracker", font=("Ariel", 26, "italic"))
        canvas.grid(row=0, column=1)
        return canvas

        def setup_page1(self):
        # ---- First Display ----#
        canvas = self.create_canvas(self.frame1)
        def on_entry_click(event):
            if entry.get() == "Enter your username":
                entry.delete(0, tk.END)
                entry.config(foreground="black")

        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, "Enter your username")
                entry.config(foreground="gray")

        entry = ttk.Entry(self.frame1, foreground="gray")
        entry.insert(0, "Enter your username")  # Insert placeholder text
        entry.bind("<FocusIn>", on_entry_click)  # Bind focus-in event
        entry.bind("<FocusOut>", on_focus_out)  # Bind focus-out event

        submit_btn = tk.Button(self.frame1, text="Submit", command=lambda: self.show_page2(entry.get()) if len(entry.get()) != 0 else username_entry.insert(0, "Input your username"))
        canvas.create_window(170, 200, window=entry, width=200, height=30)
        canvas.create_window(300, 200, window=submit_btn)

    def setup_page2(self, user):
        # ------- Second Page -------#
        canvas = self.create_canvas(self.frame2)

        canvas.create_text(50, 30, text=user, font=("Ariel", 16, "italic"))

        # -------  Placeholder handling functions  ------#
        def on_entry_click(event, entry, placeholder):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="black")

        def on_focus_out(event, entry, placeholder):
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(fg="gray")

        # Category Entry
        canvas.create_text(100, 200, text="Category:", font=("Ariel", 16, "normal"))
        category_entry = tk.Entry(self.frame2, fg="gray")
        category_placeholder = "Food, Bills, Clothing...etc"
        category_entry.insert(0, category_placeholder)
        category_entry.bind("<FocusIn>", lambda event: on_entry_click(event, category_entry, category_placeholder))
        category_entry.bind("<FocusOut>", lambda event: on_focus_out(event, category_entry, category_placeholder))

        # Amount Entry
        canvas.create_text(100, 250, text="Amount:", font=("Ariel", 16, "normal"))
        amount_entry = tk.Entry(self.frame2, fg="gray")
        amount_placeholder = "Enter amount"
        amount_entry.insert(0, amount_placeholder)
        amount_entry.bind("<FocusIn>", lambda event: on_entry_click(event, amount_entry, amount_placeholder))
        amount_entry.bind("<FocusOut>", lambda event: on_focus_out(event, amount_entry, amount_placeholder))

        # Date Entry
        canvas.create_text(100, 300, text="Date:", font=("Ariel", 16, "normal"))
        date_entry = tk.Entry(self.frame2, fg="gray")
        date_placeholder = "(dd-mm-yyyy)"
        date_entry.insert(0, date_placeholder)
        date_entry.bind("<FocusIn>", lambda event: on_entry_click(event, date_entry, date_placeholder))
        date_entry.bind("<FocusOut>", lambda event: on_focus_out(event, date_entry, date_placeholder))

        # Buttons
        expense_submit_btn = tk.Button(text="Submit", command=lambda: self.submit_expense(
            user, category_entry, amount_entry, date_entry
        ))
        calculate_expense_btn = tk.Button(text="Expenses", command=lambda: self.show_page3(user))

        # Placing the entries and labels on the canvas
        canvas.create_window(250, 200, window=category_entry, width=200, height=25)
        canvas.create_window(250, 250, window=amount_entry, width=200, height=25)
        canvas.create_window(250, 300, window=date_entry, width=200, height=25)
        canvas.create_window(270, 350, window=expense_submit_btn)
        canvas.create_window(150, 350, window=calculate_expense_btn)
          
    def setup_page3(self, user):
        canvas = self.create_canvas(self.frame3)
        if os.path.exists("ex.csv"):
            data = pd.read_csv("ex.csv")
            data_dict = data.groupby("Categories")["Amount"].sum().to_dict()
            data_dict["Total Spending"] = sum(data["Amount"].tolist())
            x1 = 120
            x2 = 270
            y = 150
            self.expenses.clear()
            for (key, value) in data_dict.items():
                if key == "Total Spending":
                    cat = canvas.create_text(x1, y, text=key, font=("Ariel", 14, "bold"))
                    amt = canvas.create_text(x2, y, text=value, font=("Ariel", 14, "bold"))
                else:
                    cat = canvas.create_text(x1, y, text=key, font=("Ariel", 12, "normal"))
                    amt = canvas.create_text(x2, y, text=value, font=("Ariel", 12, "normal"))
                self.expenses.append(cat)
                self.expenses.append(amt)
                y += 50
            back_btn = tk.Button(text="back...", command=lambda: self.show_page2(user))
            canvas.create_window(200, 350, window=back_btn)
        else:
            print("You don't have any expense file, input necessary details to calculate your expenses")
    def submit_expense(self, user, category, amount, date):
        if len(category.get()) != 0 and len(amount.get()) != 0 and len(date.get()) != 0:
            ExpenseTracker(
                user,
                category.get(),
                amount.get(),
                date.get()
            )
            category.delete(0, tk.END)
            amount.delete(0, tk.END)
            date.delete(0, tk.END)
        else:
            category.insert(0, "Needed: ")
            amount.insert(0, "Needed")
            date.insert(0, "Needed: ")


    def show_page1(self):
        self.frame1.grid(row=0, column=0, sticky="nsew")


    def show_page2(self, username):
        self.frame1.destroy()
        self.frame3.grid_forget()
        self.setup_page2(username)
        self.frame2.grid(row=0, column=0, sticky="nsew")

    def show_page3(self, username):
        self.frame2.grid_forget()
        self.setup_page3(username)
        self.frame3.grid(row=0, column=0, sticky="nsew")


rt = tk.Tk()
rt.title("Expense Tracker")
bg_img = PhotoImage(file="bg.png")
app = ExpenseTrakerApp(rt, bg_img)
rt.mainloop()
