# Try and Except Blocks
Example 1

Input: 5 / 0
result = 5 / 0
print(result)

# Example 2
try:
    result = 5 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Example 3
try:
    print(unknown_variable)
except NameError as error:
    print("An error occurred, this is the detailed error message from Python: " + str(error))

# Example 4
try:
    result = 5 / 0
    print(unknown_variable)
except NameError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
except Exception:
    print("An error happened :(")
