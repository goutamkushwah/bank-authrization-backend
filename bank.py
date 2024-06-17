
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
username = int(input("Enter account no: "))
pass1 = int(input("Enter the password: "))
account_found = None
for acc in accounts:
    if acc["account"] == username and acc["password"] == pass1:
        account_found = acc
        break

if account_found:
    test = int(input("Enter your choice \n 1. Details, 2. Cash Withdrawal, 3. Cash Deposit: "))
    if test == 1:
        print("Account holder:", account_found["holder"])    
        print("Amount:", account_found["amount"])
    elif test == 2:
        cash = int(input("How much cash do you want to withdraw? "))
        if cash <= account_found["amount"]:
            account_found["amount"] -= cash
            print("Withdrawal successful!")
            print("Total Amount:", account_found["amount"])
        else:
            print("Insufficient balance.")
    elif test == 3:
        cash = int(input("How much cash do you want to deposit? "))
        account_found["amount"] += cash
        print("Deposit successful!")
        print("Total Amount:", account_found["amount"])
    else:
        print("Invalid choice.")
else:
    print("Wrong password")