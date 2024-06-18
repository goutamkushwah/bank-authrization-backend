import tkinter as tk
from tkinter import messagebox

# Backend logic
accounts = [
    {"holder": "Goutam Kushwah", "account": 2111975, "password": 110903, "amount": 2000000},
    {"holder": "Diksha Kushwah", "account": 2111976, "password": 220902, "amount": 1500000},
     {"holder": "Devang Kushwah", "account": 2111977, "password": 4092001, "amount": 1500000},
    {"holder": "Shivam Kushwah", "account": 2111978, "password": 654321, "amount": 1500000},
    {"holder": "Shantilal Kushwah", "account": 2111979, "password": 544321, "amount": 1500000},
    {"holder": "Sudha Kushwah", "account": 2111980, "password": 654345, "amount": 1500000},
    {"holder": "Babulal Kushwah", "account": 2111981, "password": 654365, "amount": 1500000},
    {"holder": "Chanchala Kushwah", "account": 2111982, "password": 654395, "amount": 1500000},
    {"holder": "Asharam Kushwah", "account": 2111983, "password": 654375, "amount": 1500000},
    # Add more accounts as needed
]

# Global variable to keep track of the current account after login
current_account = None

# Function to find account
def find_account(username, password):
    for acc in accounts:
        if acc["account"] == username and acc["password"] == password:
            return acc
    return None

# Function to handle login
def login():
    global current_account
    username = int(account_entry.get())
    password = int(password_entry.get())
    account = find_account(username, password)
    if account:
        current_account = account
        messagebox.showinfo("Login Success", f"Welcome {account['holder']}!")
        # Hide login frame and show operations frame
        login_frame.pack_forget()
        operation_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Wrong account number or password")

# Function to handle withdrawal
def withdraw():
    cash = int(cash_entry.get())
    if cash <= current_account["amount"]:
        current_account["amount"] -= cash
        messagebox.showinfo("Success", f"Withdrawal successful! total balance: {current_account['amount']}")
    else:
        messagebox.showerror("Error", "Insufficient balance.")

# Function to handle deposit
def deposit():
    cash = int(cash_entry.get())
    current_account["amount"] += cash
    messagebox.showinfo("Success", f"Deposit successful! total balance: {current_account['amount']}")

# Function to display account details
def display_details():
    messagebox.showinfo("Account Details", f"Holder: {current_account['holder']}\nAmount: {current_account['amount']}")

# Create the main window
root = tk.Tk()
root.title("Banking System")

# Login frame
login_frame = tk.Frame(root)
login_frame.pack()

account_label = tk.Label(login_frame, text="Account No:")
account_label.pack()
account_entry = tk.Entry(login_frame)
account_entry.pack()

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

# Operation frame (hidden initially)
operation_frame = tk.Frame(root)

details_button = tk.Button(operation_frame, text="Display Details", command=display_details)
details_button.pack()

cash_label = tk.Label(operation_frame, text="Enter amount:")
cash_label.pack()
cash_entry = tk.Entry(operation_frame)
cash_entry.pack()

withdraw_button = tk.Button(operation_frame, text="Withdraw", command=withdraw)
withdraw_button.pack()

deposit_button = tk.Button(operation_frame, text="Deposit", command=deposit)
deposit_button.pack()

# Start the GUI loop
root.mainloop()

