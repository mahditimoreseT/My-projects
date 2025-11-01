# tarif list daneshjuyan
students_list = [
    {"student_id": 1, "name": "Ali", "grades": [18, 19, 20]},
    {"student_id": 2, "name": "Zahra", "grades": [15, 14, 16.5]},
    {"student_id": 3, "name": "Mehdi", "grades": [17, 18, 19]},
]

# tabe mohasbeh madel  daneshju
def calculate_student_gpa(student):
    grades = student["grades"]
    gpa = sum(grades) / len(grades)
    return gpa

# halgheh baraye namayesh madel  daneshju
for student in students_list:
    avg = calculate_student_gpa(student)
    print(f"Name: {student['name']} | GPA: {avg:.2f}")
