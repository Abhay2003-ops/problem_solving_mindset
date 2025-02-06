# Program to evaluate student performance based on exam score

# Step 1: Process for taking score input from user
score_input = input("Please enter your exam score (0-100): ")

# Step 2: Try to convert the input to an integer.
try:
    score = int(score_input)
except ValueError:
    # If the input is not a valid integer, print an error message
    print("Invalid input! Please enter a valid number.")
    score = None

# Step 3: Run conditional checks if score is valid
if score is not None:
    # First, we should check the range of the score since exam scores should be between 0 and 100.
    if score < 0 or score > 100:
        print("Score should be between 0 and 100.")
    else:
        # Now, based on the score, display the appropriate message using conditional statements:
        if score < 50:
            # If the score is less than 50, the student will receive a "Needs Improvement" message.
            print("Result: Needs Improvement")
        elif score < 75:
            # If the score is more than 50 but less than 75, a "Good" message will be displayed.
            print("Result: Good")
        else:
            # If the score is 75 or more, the student will receive an "Excellent" message.
            print("Result: Excellent")
