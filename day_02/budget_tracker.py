while True:
    budget_input = input("Enter your total monthly budget (or 'exit' to quit): Rs.")
    if budget_input.lower() == "exit":
        print("Goodbye!")
        break
    budget = float(budget_input)

    expense1 = float(input("Enter expense 1 amount: Rs."))
    expense2 = float(input("Enter expense 2 amount: Rs."))
    expense3 = float(input("Enter expense 3 amount: Rs."))

    total_expenses = expense1 + expense2 + expense3
    remaining = budget - total_expenses

    print(f"\nTotal Budget:    Rs.{budget:.2f}")
    print(f"Total Expenses:  Rs.{total_expenses:.2f}")
    print(f"Remaining Balance: Rs.{remaining:.2f}")

    if remaining < 500:
        print("Warning: Low Funds")
