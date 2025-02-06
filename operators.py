#logical operators  with multiplesd conditions
# checking pass/fail based on student score
#combination of logical operators
#using 'not' operator

# Taking input from the user
student_score = int(input("Enter student score: "))
student_attendance = int(input("Enter student attendance: "))
extra_credit_completed = input("Did the student complete extra credit? (yes/no): ").strip().lower() == "yes"

# Checking conditions
if (student_score > 50) and (student_attendance > 75):
    print("Logical Operators:")
    print("Condition: Student score and attendance are sufficient.")
    print("Result: Pass")
else:
    print("Logical Operators:")
    print("Condition: Either student score or attendance is insufficient.")
    print("Result: Fail")

if (student_score > 90) or extra_credit_completed:
    print("\nResult: Excellent")
else:
    print("\nResult: Needs Improvement")

print("\nUsing 'not' operator:")
if not (student_score < 50):
    print("Student did not score less than 50. (i.e., score is 50 or above)")
else:
    print("Student scored less than 50.")

print("\n----------------------------------------\n")



