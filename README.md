# Expense Tracker

A simple **Tkinter-based Expense Tracker** that allows users to record, view, and manage their expenses. The application stores expense data in a CSV file and provides an easy-to-use graphical interface.

## 📌 Features

- **User Authentication**: Users enter their name to track expenses.
- **Expense Entry**: Add expenses with category, amount, and date.
- **Data Persistence**: Saves expenses in `ex.csv`.
- **Expense Summary**: Calculates total expenses per category.
- **Graphical UI**: Built using `Tkinter` for an interactive experience.

## 🚀 Installation

### Prerequisites
Ensure you have Python installed (version 3.x).

1. Clone the repository:
   ```sh
   git clone https://github.com/DanielXDev/Expense-Tracker.git
   cd expense-tracker
   ```

2. Install required dependencies:
   ```sh
   pip install pandas
   ```

3. Run the application:
   ```sh
   python expense_ui_app.py
   ```

## 🛠 Usage

1. **Launch the app**
2. **Enter your name** and press `Submit`
3. **Add an expense** by selecting a category, entering an amount, and specifying the date
4. **View total expenses** by pressing the `Expenses` button

## 📂 Project Structure
```
expense-tracker/
│-- expense_ui_app.py                 # Main UI implementation
│-- expense_tracker.py    # Expense tracking logic
│-- ex.csv                # CSV file for storing expenses (created automatically)
│-- bg.png                # Background image for UI
│-- README.md             # Project documentation
```

## 💡 Future Improvements
- ✅ Add charts for visualizing expenses
- ✅ Implement SQLite database for better data management
- ✅ Enhance UI with more themes and icons
- ✅ Total expense sorted by amount,date(monthly,yearly)


## 🤝 Contributing
Pull requests are welcome! If you have ideas for improvements, please create an issue or fork the project.

## 📜 License
This project is open-source and available under the **MIT License**.

---

🌟 *Star this repo if you find it helpful!* 🌟

