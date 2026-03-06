budget = float(input("Enter your total monthly budget: $"))

expense1 = float(input("Enter expense 1 amount: $"))
expense2 = float(input("Enter expense 2 amount: $"))
expense3 = float(input("Enter expense 3 amount: $"))

total_expenses = expense1 + expense2 + expense3
remaining = budget - total_expenses

print(f"\nTotal Budget:    ${budget:.2f}")
print(f"Total Expenses:  ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining:.2f}")

if remaining < 500:
    print("Warning: Low Funds")
