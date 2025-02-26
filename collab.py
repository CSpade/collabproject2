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
