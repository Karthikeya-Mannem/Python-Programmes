num = int(input("Enter Number : "))

num_str = str(num)
num_digits = len(num_str)

sum_of_powers = 0
temp_num = num

while temp_num > 0:
    digit = temp_num%10
    sum_of_powers += digit**num_digits
    temp_num //= 10

if sum_of_powers == num:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")