# /////////////////////////////////////////////////////////
class Vehicle:
    def __init__(self, vehicle_brand, manufacture_year):
        self.vehicle_brand = vehicle_brand
        self.manufacture_year = manufacture_year

    def display_info(self):
        print(f"Brand: {self.vehicle_brand}")
        print(f"Year: {self.manufacture_year}")


# ////////////////////////////////////////////////////////
class Car(Vehicle):
    def __init__(self, vehicle_brand, manufacture_year, number_of_doors):
        super().__init__(vehicle_brand, manufacture_year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")


# /////////////////////////////////////////////////////////
class Motorcycle(Vehicle):
    def __init__(self, vehicle_brand, manufacture_year, has_sidecar):
        super().__init__(vehicle_brand, manufacture_year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has sidecar: {self.has_sidecar}")


# ////////////////////////////////////////////////////////////////
car1 = Car("BMW", 2020, 4)
motorcycle1 = Motorcycle("Honda", 2018, False)

print("Car Info:")
car1.display_info()

print("\nMotorcycle Info:")
motorcycle1.display_info()
