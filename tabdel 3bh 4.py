# تعریف کلاس دانشجو
class Student:
    def __init__(self, student_id, student_name, grades_list):
        self.student_id = student_id
        self.student_name = student_name
        self.grades_list = grades_list

    def calculate_gpa(self):
        return sum(self.grades_list) / len(self.grades_list)


# ایجاد چند شیء از کلاس Student
students_list = [
    Student(1, "Ali", [18, 19, 20]),
    Student(2, "Zahra", [15, 14, 16.5]),
    Student(3, "Mehdi", [17, 18, 19]),
]


# نمایش معدل هر دانشجو
for student in students_list:
    average_gpa = student.calculate_gpa()
    print(f"Name: {student.student_name} | GPA: {average_gpa:.2f}")
