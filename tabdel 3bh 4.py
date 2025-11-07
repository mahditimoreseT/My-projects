# تعریف کلاس دانشجو
class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades)


# ایجاد چند شیء از کلاس Student
students_list = [
    Student(1, "Ali", [18, 19, 20]),
    Student(2, "Zahra", [15, 14, 16.5]),
    Student(3, "Mehdi", [17, 18, 19]),
]


# نمایش معدل هر دانشجو
for student in students_list:
    avg = student.calculate_gpa()
    print(f"Name: {student.name} | GPA: {avg:.2f}")
