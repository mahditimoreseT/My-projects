class FoodItem:
    def __init__(self,name,base_price):

        self.name=name
        self.base_price=base_price

        if base_price>0:
            self._base_price=base_price
        else:
            self._base_price=0


    def calculate_cost(self):
        return self._base_price
    
    def __str__(self):
        return self.name
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Pizza(FoodItem):
    def __init__(self, name, base_price,size):
        super().__init__(name, base_price)

        self.size=size.lower()
        self.extra_toppings={}

    def extra_topping(self,key_nam,value_gmat):
        self.extra_toppings[key_nam]=value_gmat

    def calculate_cost(self):
        gymat=self._base_price

        if self.size == "medium":
            gymat *= 1.2
        elif self.size == "large":
            gymat *= 1.5

        total=sum(self.extra_toppings.values())

        return gymat+total 
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Burger(FoodItem):
    def __init__(self, name, base_price,is_double):
        super().__init__(name, base_price)
        self.is_double=is_double

    def calculate_cost(self):
        mablag=self._base_price
        if self.is_double:
            mablag+=(mablag*0.35)
        return mablag
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Order:
    def __init__(self):
        self.listm=[]
    def add_food(self,food):
        self.listm.append(food)

    def print_receipt(self):
        self.totali=0

        for i in self.listm:
            s=i.calculate_cost()
            self.totali+=s
            print(i.name,s)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


p = Pizza("Margarita", 200, "Large")
p.extra_topping("Cheese", 30)

b = Burger("Double Burger", 150, True)

o = Order()
o.add_food(p)
o.add_food(b)
o.print_receipt()
