from datetime import datetime
expenses = {}
def add_expense():
   category = input("Enter expense category: ")
   amount = float(input("Enter expense amount: "))
   while amount <= 0:
       print("Amount must be positive.")
       amount = float(input("Enter expense amount: "))
   date = input("Enter expense date (YYYY-MM-DD): ")
   while True:
       try:
           datetime.strptime(date, '%Y-%m-%d')
           break
       except ValueError:
           print("Invalid date format. Please use YYYY-MM-DD.")
           date = input("Enter expense date (YYYY-MM-DD): ")
  
   expenses.setdefault(category, []).append({"amount": amount, "date": date})
   print(f"Expense of {amount} added to category '{category}' on {date}.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for category, expense_list in expenses.items():
        print(f"\nCategory: {category}")
        for expense in expense_list:
            print(f" - Amount: {expense['amount']}, Date: {expense['date']}")

def calculate_total_expenses():
    total = sum(expense['amount'] for expenses_list in expenses.values() for expense in expenses_list)
    print(f"\nTotal expenses: {total}")

def delete_expense():
    category = input("Enter expense category to delete: ")
    date = input("Enter date of expense to delete (YYYY-MM-DD): ")
    if category not in expenses:
        print(f"Category '{category}' does not exist.")
        return
    expenses[category] = [e for e in expenses[category] if e['date'] != date]
    print(f"Expense on {date} in category '{category}' removed.")

