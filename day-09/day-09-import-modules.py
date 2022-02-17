# Import Modules
# Example 1
import os
print(os.listdir())

# Example 2
print(os.getcwd())

# Example 3
import operator
import os
print(os.getcwd())
print(operator.add(5,6))
print(operator.sub(5,6))
print(operator.mul(5,6))
print(operator.truediv(5,6))

# Example 4
import math
print(math.pow(5,6))
print(math.sqrt(25))
print(math.fabs(-8))
print(math.gcd(48,36))

# Example 5
from operator import add
print(add(5, 6))

# Example 6 -
import operator as ops
print(ops.add(10,10))

# Example 7 - View the functions of a module
import math
functions = dir(math)
print(functions)