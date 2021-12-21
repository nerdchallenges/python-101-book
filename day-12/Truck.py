# Example 5 - Building a Truck class
from Car import Car
class Truck(Car):
    def __init__(self,year, make, model, color, is_sedan, mpg, tank_size, cab_seating, tow_capacity):
        super().__init__(year, make, model, color, is_sedan, mpg, tank_size)
        self.cab_seating = cab_seating
        self.tow_capacity = tow_capacity


