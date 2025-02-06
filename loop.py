
students_scores = []


while True:
    name = input("Enter student's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    score = int(input(f"Enter {name}'s score: "))
    students_scores.append((name, score))


print("\nStudent Grades:")


for student, score in students_scores:

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    

    print(f"{student}: {grade}")

print("\nStudents with Index (using enumerate):")

for index, (student, score) in enumerate(students_scores, start=1):

    print(f"{index}. {student} - Score: {score}")


