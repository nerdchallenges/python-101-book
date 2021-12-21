# Try / Except
# Example 1
try:
    result = 5 / 0
except Exception as error:
    print(error)
else:
    print(result)

# Example 2
try:
    result = 5 / 0
except Exception as error:
    print(error)
else:
    print(result)
finally:
    print("This program runs even if exceptions occur.")
