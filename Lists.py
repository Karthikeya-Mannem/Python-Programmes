list = [1,4,2,6,5]

print(list[0])
list[0] = 0

list.append(10)
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(1,20)
print(list)

list.pop(6)
print(list)