def cal_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater%x == 0) and (greater%y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

x = int(input("Enter the number 1 : "))
y = int(input("Enter the number 2 : "))

res = cal_lcm(x,y)
print(f"The LCM of {x} and {y} is {res}")