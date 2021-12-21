# User defined functions
# Example 1
def function_name():
    print("my first user-defined function!")

function_name()
function_name()
function_name()
function_name()

# Example 2
def welcome_msg():
    print("Welcome to Python 101")

welcome_msg()

# Example 3
def welcome_msg(name):
    print(f"Welcome to Python 101, {name}")

welcome_msg("Casey")
welcome_msg("Rico")
welcome_msg("Mia")
welcome_msg("Marilyn")
welcome_msg("Jenny")

# DRY - Don't Repeat Yourself
# Example 4
def welcome_msg(title, name):
    print(f"Welcome to {title}, {name}")

welcome_msg("Python 101", "Casey")

# Example 5
def welcome_msg(title, name, isbn='NoISBN'):
    print(f"Welcome to {title}, {name}. The ISBN for the book is: {isbn}")

welcome_msg("Python 101", "Rico", isbn="1234567")
welcome_msg("Python 101", "Mia")
welcome_msg("Python 101", "Jenny")

