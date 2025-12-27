# /////////////////////////////////////////////
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(self.title, self.price, self.author)

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount


# /////////////////////////////////////////////
book1 = Book("A", "b", 3000)
book2 = Book("Z", "x", 4000)

book1.display_details()
book2.display_details()

book2.apply_discount(10)

book1.display_details()
book2.display_details()
