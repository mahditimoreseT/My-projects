# //////////////////////////////////////////////
class Contact:
    def __init__(self, contact_name, contact_phone_number):
        if not contact_phone_number.isdigit():
            raise ValueError("input number ok")

        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number


# //////////////////////////////////////////
class PhoneBook:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact_name, contact_phone_number):
        new_contact = Contact(contact_name, contact_phone_number)
        self.contact_list.append(new_contact)

    def save_to_csv(self, file_name):
        file = open(file_name, "w", encoding="utf-8")

        for contact in self.contact_list:
            file.write(
                contact.contact_name + "," +
                contact.contact_phone_number + "\n"
            )

        file.close()

    def load_from_csv(self, file_name):
        try:
            file = open(file_name, "r", encoding="utf-8")
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.strip()
                line_parts = line.split(",")

                try:
                    contact_name = line_parts[0]
                    contact_phone_number = line_parts[1]

                    new_contact = Contact(
                        contact_name,
                        contact_phone_number
                    )
                    self.contact_list.append(new_contact)

                except ValueError:
                    pass

        except FileNotFoundError:
            print("file created ok")


# ///////////////////////////////////////////////////////////
phone_book = PhoneBook()
phone_book.load_from_csv("contacts.csv")


# ///////////////////////////////////////////////////////////
while True:
    print("1 - add contact")
    print("2 - print contacts")
    print("3 - save & exit")

    try:
        user_choice = int(input("?: "))
    except ValueError:
        print("enter number")
        continue

    if user_choice == 1:
        input_name = input("name: ")
        input_phone_number = input("phone number: ")

        try:
            phone_book.add_contact(
                input_name,
                input_phone_number
            )
            print("add ok")
        except ValueError:
            print("oh no please again")

    elif user_choice == 2:
        if len(phone_book.contact_list) == 0:
            print("no users")
        else:
            for contact in phone_book.contact_list:
                print(
                    contact.contact_name,
                    "-",
                    contact.contact_phone_number
                )

    elif user_choice == 3:
        phone_book.save_to_csv("contacts.csv")
        print("save ok & bye")
        break

    else:
        print("number not valid")
