# Part 2 - Using the Car class :D
from Car import Car

# car_a = Car("2021", "Tesla", "Model S", "Red", True)
# print(f"The color of the car is: {car_a.color}")
# print(f"Is this car a Sedan, True or False?: {car_a.is_sedan}")
# print(car_a)
# print(Car)

# # Part 3 / Example 3 - Adding multiple `instances` aka cars
# car_a = Car("2021", "Tesla", "Model S", "Red", True)
# car_b = Car("2021", "Mazda", "CX-5", "Black", True)
# car_c = Car("2020", "Cadillac", "CTS", "Black", False)
# car_d = Car("2021", "Tesla", "Model S", "Red", True)

# color_list = [car_a.color, car_b.color, car_c.color]

# count = 0
# for color in color_list:
#     if color == "Black":
#         count += 1
#         # count = count + 1
# print(f"The number of Black cars in inventory is: {count}")
# print(f"The colors of those cars are: {color_list}")

# print(car_a == car_b)
# print(car_a == car_d)
# print(car_a)
# print(car_d)

# Example 4 - Calling the method calculate_total_miles()
hybrid = Car("2021", "Chevy", "Impala Hybrid", "Black", False, 60, 15)

# print(hybrid.calculate_total_miles())

# Example 5 - Build an F150
from Truck import Truck
f150 = Truck("2021", "Ford", "F150", "Black", False, 15, 25, True, 5000)

print(f150)
print(f150.cab_seating)
print(f150.tow_capacity)
print(f150.color)
print(f150.calculate_total_miles())

print(isinstance(f150, Truck))
print(isinstance(f150, Car))
print(isinstance(f150, int))
print(isinstance(f150, object))

# Example 6
hybrid = Car("2021", "Chevy", "Impala Hybrid", "Black", False, 60, 15)
f150 = Truck("2021", "Ford", "F150", "Black", False, 15, 25, True, 5000)
print(f150)
print(hybrid.__doc__)