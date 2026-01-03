#----
class Contact:
    def __init__(self, name, phone):
        if not phone.isdigit():
            raise ValueError("Phone must be digits")
        self.name = name
        self.phone = phone
#----
class PhoneBook:
    def __init__(self):
        self.contacts = []

#+++++
    def add(self, name, phone):
        if not name.strip(): 
            return
        new_person = Contact(name, phone)
        self.contacts.append(new_person)
#+++++
    def delete(self, name):
        new_contacts = []  
        for c in self.contacts:
            if c.name != name: 
                new_contacts.append(c) 
        self.contacts = new_contacts 
#+++++
    def search(self, text):
        search_results = [] 
        text_lower = text.lower() 
        
        for c in self.contacts:
            name_lower = c.name.lower() 
            if text_lower in name_lower: 
                search_results.append(c)
        
        return search_results
#+++++
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for c in self.contacts:
                line = c.name + "," + c.phone + "\n"
                f.write(line)
#+++++
    def load(self, filename):
        self.contacts = [] 
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        name = parts[0]
                        phone = parts[1]
                        contact_obj = Contact(name, phone)
                        self.contacts.append(contact_obj)
        except FileNotFoundError:
            pass
#----