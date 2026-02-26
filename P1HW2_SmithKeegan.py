#Keegan Smith
# 02/26/2026
# Travel Budget Calculator
# This program calculates total travel expenses and determines the remaining budget.

"""
PSEUDOCODE (Program Logic)

1. Start program
2. Ask user to enter total budget
3. Ask user to enter travel destination
4. Ask user to enter amount to spend on gas
5. Ask user to enter amount to spend on accommodation
6. Ask user to enter amount to spend on food
7. Add gas, accommodation, and food to calculate total expenses
8. Subtract total expenses from budget to calculate remaining balance
9. Display destination, budget, total expenses, and remaining balance
10. End program
"""

# Ask user to enter their budget
budget = float(input("Enter your total budget for the trip: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas = float(input("Enter the amount you will spend on gas: "))

# Ask user for amount they will spend on accommodation
accommodation = float(input("Enter the amount you will spend on accommodation: "))

# Ask user for amount they will spend on food
food = float(input("Enter the amount you will spend on food: "))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining_balance = budget - total_expenses

# Display results
print("\n--- Travel Budget Summary ---")
print(f"Destination: {destination}")
print(f"Total Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")