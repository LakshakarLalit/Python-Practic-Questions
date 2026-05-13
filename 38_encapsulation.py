class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " #"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = Electric_car("Tesla", "Model S", "85 kwh")

print(my_tesla.get_brand())