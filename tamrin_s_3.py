
# تابع محاسبه معدل دانشجو
def calculate_student_gpa(student):
    grades = student["grades_list"]
    gpa = sum(grades) / len(grades)
    return gpa

# تعریف لیست دانشجویان
students_list = [
    {"student_id": 1, "student_name": "Ali", "grades_list": [18, 19, 20]},
    {"student_id": 2, "student_name": "Zahra", "grades_list": [15, 14, 16.5]},
    {"student_id": 3, "student_name": "Mehdi", "grades_list": [17, 18, 19]},
]
# حلقه برای نمایش معدل دانشجویان
for student in students_list:
    average_gpa = calculate_student_gpa(student)
    print(f"Name: {student['student_name']} | GPA: {average_gpa:.2f}")
