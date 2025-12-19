# //////////////////////////////////////////////
class Contact:
    def __init__(self, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError("inpiut number ok")
        self.name = name
        self.phone_number = phone_number
#//////////////////////////////////////////
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def save_to_csv(self, filename):
        file = open(filename, "w", encoding="utf-8")
        for c in self.contacts:
            file.write(c.name + "," + c.phone_number + "\n")
        file.close()

    def load_from_csv(self, filename):
        try:
            file = open(filename, "r", encoding="utf-8")
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.strip()
                parts = line.split(",")

                try:
                    name = parts[0]
                    phone = parts[1]
                    contact = Contact(name, phone)
                    self.contacts.append(contact)
                except ValueError:
                    pass

        except FileNotFoundError:
            print("created ok")
#///////////////////////////////////////////////////////////
phonebook = PhoneBook()
phonebook.load_from_csv("contacts.csv")
#//////////////////////////////////////////////////////////////
while True:
    print("1-add")
    print("2-print")
    print("3-S&E")
    try:
        choice = int(input("?: "))
    except ValueError:
        print(" entre number")
        continue
    if choice == 1:
        name = input("name: ")
        phone = input("number p : ")
        try:
            phonebook.add_contact(name, phone)
            print("add ok")
        except ValueError:
            print("oh no plese agan")

    elif choice == 2:
        if len(phonebook.contacts) == 0:
            print("not user")
        else:
            for c in phonebook.contacts:
                print(c.name, "-", c.phone_number)

    elif choice == 3:
        phonebook.save_to_csv("contacts.csv")
        print("Save ok & bay")
        break

    else:
        print(" number namotabar ast hoshshshshsa")
#payan poroject ba 79 khat;