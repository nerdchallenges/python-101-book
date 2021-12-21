debugger = "A debugger is a tool that lets you find problems or bugs with your code"
print("Welcome to this fake program")
print(f"We will use it to talk about a debugger.")
print(f"{debugger}")

add = 5 + 5
print(add)


def some_cool_function(x, y):
    result = x * y
    return result


run_this = some_cool_function(3, 3)
print(f"{run_this}")

user_x = int(input('Enter a number you want to times by 2 > '))
user_result = some_cool_function(user_x, 2)
print(f"{user_result}")
