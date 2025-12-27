def calculate_average(grades_list):
    return sum(grades_list) / len(grades_list)


number_of_courses = int(input("تعداد درس‌ها: "))

grades = []
for i in range(number_of_courses):
    grade = float(input(f"نمره درس {i + 1}: "))
    grades.append(grade)

average_grade = calculate_average(grades)

print(f"میانگین: {average_grade:.2f}")

if average_grade >= 17:
    print("خوب")
elif average_grade >= 10:
    print("قابل قبول")
else:
    print("ضعیف")
