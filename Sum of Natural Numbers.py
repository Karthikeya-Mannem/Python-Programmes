limit = int(input("Enter Limit : "))

sum = 0
for i in range(1,limit+1):
    sum = sum+i

print(f"The Sum of {limit} Natural Numbers : {sum}")