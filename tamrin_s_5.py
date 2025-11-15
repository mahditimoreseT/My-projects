#////////////////////////////////////
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []  
#////////////////////////////////////
    def add_grade(self, grade):
        if 0 <= grade <= 20:
            self._grades.append(grade)
        else:
            print("خطا: نمره باید بین 0 تا 20 باشد!")
#////////////////////////////////////
    def get_grades(self):
        return self._grades
#////////////////////////////////////
    def calculate_gpa(self):
        grades = self.get_grades()
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)
#////////////////////////////////////
    def __str__(self):
        return f"دانشجو: {self.name} | معدل: {self.calculate_gpa():.2f}"
#////////////////////////////////////
student1 = Student("Reza Amini", 101)

student1.add_grade(18)
student1.add_grade(20)
student1.add_grade(12)
student1.add_grade(25) 

print(student1)

print(student1.get_grades())
print("GPA:", student1.calculate_gpa())