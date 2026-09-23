expenses = []

for i in range(5):
    expense = float(input(f"Enter expense {i + 1}: "))
    expenses.append(expense)

total = sum(expenses)
average = total / len(expenses)

print("\n--- Expense Summary ---")
print("Expenses:", expenses)
print("Total Expense:", total)
print("Average Expense:", average)