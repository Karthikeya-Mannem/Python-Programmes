def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))
    
nterms = int(input("Enter the number of Terms : "))
if nterms <= 0:
    print("Please Enter Positive Integer")
else:
    print("Fibonacci Series : ")
    for i in range(nterms):
        print(recur_fibo(i))