import math
num = float(input("Enter a number: "))
if num > 0:
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
else:
    sqrt_result = "Undefined (number must be non-negative)"
    log_result = "Undefined (number must be positive)"
sine_result = math.sin(num)
print("Square root:", sqrt_result)
print(" logarithm :", log_result)
print("Sine:", sine_result)
