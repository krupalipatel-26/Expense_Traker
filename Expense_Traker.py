import os

FILE_NAME = "expenses.txt"

# Load expenses from file
def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({
                    "category": category,
                    "amount": float(amount)
                })

    return expenses

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")

# Add expense
def add_expense(expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "category": category,
        "amount": amount
    })

    save_expenses(expenses)

    print("Expense added successfully!")

# View expenses
def view_expenses(expenses):

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== Expenses =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} - ₹{expense['amount']}"
        )

# Total expenses
def total_expenses(expenses):

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(f"\nTotal Expenses: ₹{total}")

# Main Program
expenses = load_expenses()

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expenses(expenses)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")