import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Note"])

def add_transaction():
    trans_type = input("Type (Income/Expense): ").strip().capitalize()
    category = input("Category (e.g., Food, Salary, Rent): ").strip()
    amount = float(input("Amount: "))
    note = input("Note (optional): ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, trans_type, category, amount, note])
    print("Transaction added successfully!\n")

def show_summary():
    income = 0
    expenses = 0

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            if row["Type"] == "Income":
                income += amount
            elif row["Type"] == "Expense":
                expenses += amount

    balance = income - expenses
    print(f"\n--- Summary ---")
    print(f"Total Income : ₹{income:.2f}")
    print(f"Total Expenses: ₹{expenses:.2f}")
    print(f"Net Balance  : ₹{balance:.2f}\n")

def list_transactions():
    print("\n--- All Transactions ---")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))
    print()

def main():
    initialize_csv()
    while True:
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View All Transactions")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            list_transactions()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
