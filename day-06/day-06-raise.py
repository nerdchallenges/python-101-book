# Raising an exception, manually
# Example 1
user_input = 1234
try:
    if not type(user_input) is int:
        raise TypeError("Please only use integers!")
    result = 5 / user_input
except TypeError as error:
    print(f"{error}")
else:
    print(f"Thanks for inputting a number, here's the result: {result}")