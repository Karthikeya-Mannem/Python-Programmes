import math

num = float(input("Enter a Number : "))

if num <= 0:
    print("please Enter aa Positive number")
else:
    result =math.log(num)
    print(f"The natural logarithm of {num} is: {result}")