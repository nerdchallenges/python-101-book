user = input("What is your name?")
print("Welcome " + user + " to the Python Calculator Program!")
calculator = input("Please choose which calculator to use: Simple or Advanced. ")
if calculator.lower() == "simple":
    op = input("Would you like to (add, subtract, multiply, or divide) two numbers?  ")
    num1 = input("Provide your first number: ")
    num2 = input("Provide your second number: ")
    if op.lower() == "add":
        print(float(num1) + float(num2))
    elif op.lower() == "subtract":
        print(float(num1) - float(num2))
    elif op.lower() == "multiply":
        print(float(num1) * float(num2))
    elif op.lower() == "divide":
        try:
            print(float(num1) / float(num2))
        except ZeroDivisionError as error:
            print(error)
    else:
        print("Invalid op or #, expected a value of add, subtract, multiply, divide, number")
elif calculator == "Advanced" or "advanced":
    print("The Advanced Calculator is still under development. Please use Simple calculator. ")
else:
    print("The input you chose is invalid. Please run program again")