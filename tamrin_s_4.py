#/////////////////////////////////////////////
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display_details(self):
        print(self.title,self.price,self.author)

    def apply_discount(self,takhfif):
        jadid=(takhfif/100)*self.price
        self.price-=jadid
        
#/////////////////////////////////////////////
a1=Book("A","b",3000)
a2=Book("Z","x",4000)

a1.display_details()
a2.display_details()

a2.apply_discount(10)

a1.display_details()
a2.display_details()

