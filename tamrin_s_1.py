print("محاسبه سن")
print("1) ساده")
print("2) حرفه‌ای")

mode = input("انتخاب حالت (1 یا 2): ")

if mode == "1":
    birth_year = int(input("سال تولد: "))
    age = 1404 - birth_year
    print("سن تقریبی:", age, "سال")

elif mode == "2":
    name = input("نام: ")
    birth_year = int(input("سال تولد: "))
    current_year = int(input("سال جاری: "))
    age = current_year - birth_year
    print("نام:", name, "| سن:", age)
