start = int(input("Enter Starting Number : "))
end = int(input("Enter Ending Number : "))

print(f"Prime Numbers between the {start} and {end} are : ")

for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            print(i)