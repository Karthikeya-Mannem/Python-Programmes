def cal_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i == 0)):
            HCF = i
    return HCF

x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))

res = cal_hcf(x,y)
print(f"The HCF of {x} and {y} is {res}")