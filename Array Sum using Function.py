def array_sum(arr):
    sum = 0
    for i in arr:
        sum = sum+i
    return sum

arr = [1,2,3]
result = array_sum(arr)
print(f"Sum of Array : {result}")