# Math Functions

# Example 1
# user_input = input("What number would you like to multiply?")
# x = int(user_input) * int(user_input)
# print(x)

# Example 2 - Build a function
# def multiply_integers(num1, num2):
#     result = num1 * num2
#     print(result)
#
#
# multiply_integers(2, 3)
# multiply_integers(10, 10)
# multiply_integers(5, 5)

# Example 3 - Calculate the area of a triangle
# def triangle_area(base, height):
#     area = (0.5 * base * height)
#     print(f"The area of the triangle is {area}")
#
#
# triangle_area(2, 5)
# triangle_area(2, 10)
#
# triangle_area(2, 5) + triangle_area(2, 10)

# Example 4 - The return
# def triangle_area(base, height):
#     area = (0.5 * base * height)
#     return area
#
# total_area = triangle_area(2,5)
# print(f"The total area of the triangle is {total_area}")

# Example 5 - Using return summing triangle area
def triangle_area(base, height):
    area = (0.5 * base * height)
    return area

x = input("What is the base of the triangle?")
y = input("What is the height of the traingle?")
triangle1 = triangle_area(8, 3)
triangle2 = triangle_area(1, 9)
triangle3 = triangle_area(int(x), int(y))
total_area = triangle1 + triangle2 + triangle3
print(f"The area of the triangle #1 is {triangle1}")
print(f"The area of the triangle #2 is {triangle2}")
print(f"The area of the triangle #3 is {triangle3}")
print(f"The total area of ALL OF THE triangles are {total_area}")