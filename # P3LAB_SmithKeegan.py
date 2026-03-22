# P3LAB_LastnameFirstname
# Program calculates the most efficient number of coins for a given amount

# Get input
amount = float(input("Enter the amount of money as a float: "))

# Convert to cents (integer)
cents = int(round(amount * 100))

# Calculate coins
dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

# Output results (only print if > 0)
if dollars > 0:
    print(dollars, "Dollar" if dollars == 1 else "Dollars")

if quarters > 0:
    print(quarters, "Quarter" if quarters == 1 else "Quarters")

if dimes > 0:
    print(dimes, "Dime" if dimes == 1 else "Dimes")

if nickels > 0:
    print(nickels, "Nickel" if nickels == 1 else "Nickels")

if pennies > 0:
    print(pennies, "Penny" if pennies == 1 else "Pennies")

# If no coins at all
if amount == 0:
    print("No change")
