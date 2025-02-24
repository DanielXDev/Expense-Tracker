import pandas as pd
import os

class ExpenseTracker:
    def __init__(self, username,category, amount, date):
        self.username = username
        self.category = category
        self.amount = amount
        self.date = date
        self.expenses = {"Name": [], "Categories": [], "Amount": [], "Date": []}
        self.input_expense()
        self.update_csv()


    def input_expense(self):
        self.expenses["Name"].append(self.username)
        self.expenses["Categories"].append(self.category)
        self.expenses["Amount"].append(self.amount)
        self.expenses["Date"].append(self.date)

    def display_expenses(self):
        try:
            df_data = pd.read_csv("ex.csv")
            print(df_data)
        except FileNotFoundError:
            print("You do not have an expense table yet.")
        except pd.errors.EmptyDataError:
            print("Your expense table is empty.")


    def update_csv(self):
        file_exists = os.path.exists("ex.csv")
        df = pd.DataFrame(self.expenses)

        try:
            if file_exists:
                df.to_csv("ex.csv", mode='a', header=False, index=False)
            else:
                df.to_csv("ex.csv", index=False)
            print("Expense recorded successfully!")
        except Exception as e:
            print(f"Error saving to CSV: {e}")


