"""
A simple application that allows users to record and view their expenses.

Requirements:
- Allow users to add expenses (description, amount)
- Store expenses in a file (CSV or JSON)
- Display a summary of all expenses
- Allow users to delete an expense (optional)
"""
budget = []
run = True

print("Expense Tracker.\n")
print("Add an expense. Enter \"0\" to finish: ")

while run == True:
    try:
        expense = int(input())

        while expense != 0:
            budget.append(expense)
            expense = int(input())
    except ValueError:
        print("Please enter a valid number.")

    if budget == []:
        print("\nYour budget is empty.")
        run = False
    else:
        print("\nBudget")
        for j in budget:
            print(j)
        run = False