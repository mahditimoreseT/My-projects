print("mohasbh_sn ")
print("1) sadh")
print("2) hrfayy")
mode = input(" (1 ya 2): ")

if mode == "1":
    year = input(" salravardkon: ")
    year = int(year)
    age = 1404 - year
    print("sn_tagribi :", age, "sal")
       
elif mode == "2":
    name = input(" namt?: ")
    birth = input("sal__tavalodt: ")
    current = input("sal_jary_ravardkon: ")
    birth = int(birth)
    current = int(current)
    age = current - birth
    print("nam:",name,"sn", age)