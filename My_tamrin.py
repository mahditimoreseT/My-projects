class FoodItem:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

        if base_price > 0:
            self._validated_base_price = base_price
        else:
            self._validated_base_price = 0

    def calculate_cost(self):
        return self._validated_base_price

    def __str__(self):
        return self.name


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Pizza(FoodItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)

        self.size = size.lower()
        self.extra_toppings = {}

    def add_extra_topping(self, topping_name, topping_price):
        self.extra_toppings[topping_name] = topping_price

    def calculate_cost(self):
        final_price = self._validated_base_price

        if self.size == "medium":
            final_price *= 1.2
        elif self.size == "large":
            final_price *= 1.5

        toppings_total_price = sum(self.extra_toppings.values())
        return final_price + toppings_total_price


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Burger(FoodItem):
    def __init__(self, name, base_price, is_double):
        super().__init__(name, base_price)
        self.is_double = is_double

    def calculate_cost(self):
        final_price = self._validated_base_price

        if self.is_double:
            final_price += final_price * 0.35

        return final_price


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Order:
    def __init__(self):
        self.ordered_items = []

    def add_food(self, food_item):
        self.ordered_items.append(food_item)

    def print_receipt(self):
        self.total_order_price = 0

        for item in self.ordered_items:
            item_price = item.calculate_cost()
            self.total_order_price += item_price
            print(item.name, item_price)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pizza_item = Pizza("Margarita", 200, "Large")
pizza_item.add_extra_topping("Cheese", 30)

burger_item = Burger("Double Burger", 150, True)

order = Order()
order.add_food(pizza_item)
order.add_food(burger_item)
order.print_receipt()
