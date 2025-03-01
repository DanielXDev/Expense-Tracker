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
        canvas.create_text(200,160, text="Enter your username below...", font=("Ariel", 10, "normal"))
        username_entry = tk.Entry(self.frame1,bg="#ffffff")

        submit_btn = tk.Button(self.frame1, text="Submit", command=lambda: self.show_page2(username_entry.get()) if len(username_entry.get()) != 0 else username_entry.insert(0, "Input your username"))
        canvas.create_window(170, 200, window=username_entry, width=200, height=30)
        canvas.create_window(300, 200, window=submit_btn)

    def setup_page2(self, user):
        # ------- Second Page -------#
        canvas = self.create_canvas(self.frame2)

        canvas.create_text(50, 30, text=user, font=("Ariel", 16, "italic"))

        canvas.create_text(100, 200, text="Category:", font=("Ariel", 16, "normal"))
        category_entry = tk.Entry(self.frame2)
        category_entry.insert(0, "Food,Bills,Clothing...etc")

        canvas.create_text(100, 250, text="Amount:", font=("Ariel", 16, "normal"))
        amount_entry = tk.Entry(self.frame2)

        canvas.create_text(100, 300, text="Date:", font=("Ariel", 16, "normal"))
        date_entry = tk.Entry(self.frame2)
        date_entry.insert(0, "(dd-mm-yyyy)")

        expense_submit_btn = tk.Button(text="Submit", command=lambda: self.submit_expense(
            user,
            category_entry,
            amount_entry,
            date_entry
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
bg_img = PhotoImage(file="bg.png")
app = ExpenseTrakerApp(rt, bg_img)
rt.mainloop()
