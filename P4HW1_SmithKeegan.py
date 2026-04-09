# Your Name
# Date
# P4HW1 - Score List and Grade Calculator
# This program collects scores, validates input, drops the lowest score,
# calculates the average, and assigns a letter grade.

# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

scores = []

# Loop to collect scores
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))

        # Validate score
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i+1} again:")

# Calculate results
lowest = min(scores)
scores.remove(lowest)

average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score : {lowest}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade : {letter_grade}")
print("--------------------------------")
