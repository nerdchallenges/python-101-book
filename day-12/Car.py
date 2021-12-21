# Part 1 - Building the class / AKA the Blueprint
# class Car:
#     def __init__(self, year, make, model, color, is_sedan):
#         self.year = year
#         self.make = make
#         self.mode = model
#         self.color = color
#         self.is_sedan = is_sedan

# Part 4 - Building more methods
# class Car:
#     def __init__(self, year, make, model, color, is_sedan, mpg, tank_size):
#         self.year = year
#         self.make = make
#         self.mode = model
#         self.color = color
#         self.is_sedan = is_sedan
#         self.mpg = mpg
#         self.tank_size = tank_size

#     def calculate_total_miles(self):
#         return self.mpg * self.tank_size

# Example 6 - Magic Methods
class Car:
    """This is a Car Class, you can build a Car Object!"""
    def __init__(self, year, make, model, color, is_sedan, mpg, tank_size):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.is_sedan = is_sedan
        self.mpg = mpg
        self.tank_size = tank_size

    def __str__(self):
        message = f"This car was built in {self.year} and is a {self.make} {self.model}. It is {self.color} and gets {self.mpg} Miles Per Gallon."
        return message

    def calculate_total_miles(self):
        return self.mpg * self.tank_size

