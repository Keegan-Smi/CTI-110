# Keegan Smith
# 4/9/2026
# P4HW2 - Employee Pay Calculator
# This program calculates pay for multiple employees including overtime
# and displays totals when finished.

# Initialize totals
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
	name = input("Enter employee's name or \"Done\" to terminate: ")

	if name.lower() == "done":
		break

	# Get hours and pay rate
	hours = float(input(f"How many hours did {name} work? "))
	pay_rate = float(input(f"What is {name}'s pay rate? "))

	# Calculate overtime
	if hours > 40:
		overtime_hours = hours - 40
		regular_hours = 40
	else:
		overtime_hours = 0
		regular_hours = hours

	overtime_pay = overtime_hours * (pay_rate * 1.5)
	regular_pay = regular_hours * pay_rate
	gross_pay = regular_pay + overtime_pay

	# Add to totals
	total_employees += 1
	total_overtime_pay += overtime_pay
	total_regular_pay += regular_pay
	total_gross_pay += gross_pay

	# Display employee info
	print("\nEmployee name:", name)
	print()
	print("Hours Worked    Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross Pay")
	print("--------------------------------------------------------------------------------")
	print(f"{hours:<15.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}"
		  f"{overtime_pay:<15.2f}{regular_pay:<14.2f}{gross_pay:.2f}")
	print()

# Final totals
print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")