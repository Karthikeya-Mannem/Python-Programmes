nterms = int(input("Enter Number of Terms : "))

n1,n2 = 0,1
count = 0

if nterms <= 0:
    print("Please Enter a Positive Integer")
elif nterms == 1:
    print(f"Fibonacci series upto {nterms} : ")
    print(n1)
else:
    print(f"Fibonacci Series upto {nterms} : ")
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1