# Import libraries
import math
from decimal import Decimal
# Pi number
print("value of pi is: ", math.pi)
#Euler's number
print("value of e is: ", math.e)
# Square root
print("value of square root of 64 is: ", math.sqrt(64))
print("value of square root of 2 is: ", round(math.sqrt(2), 5))

# Rounding up and down
original_number = 3.14159
rounded_up = math.ceil(original_number)
rounded_down = math.floor(original_number)
print("Original number: ", original_number)
print("Rounded up: ", rounded_up)
print("Rounded down: ", rounded_down)

# Factorial 5! = 5 * 4 * 3 * 2 * 1 = 120
factorial_of_5 = math.factorial(5)
print("Factorial of 5 is: ", factorial_of_5)

dec1 = Decimal('0.1')
print("Decimal representation of 0.1 is: ", dec1)
dec2 = Decimal('0.2')
print("Decimal representation of 0.2 is: ", dec2)

percentage = 100/3
print("Percentage value of 100/3 is: ", percentage)
print("Percentage value of 100/3 is: ", round(percentage, 3))
print("Percentage value of 100/3 is: ", Decimal(percentage))