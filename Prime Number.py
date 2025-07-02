num = int(input("Enter Number : "))

flag = True

if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2,num):
        if(num%i) == 0:
            flag = False
            break

if flag:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")