student_score = int(input("Enter your score: "))

if student_score >= 90:
    grade = "A"
elif student_score >= 80:
    grade = "B"
elif student_score >= 70:
    grade = "C"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")
