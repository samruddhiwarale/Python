numbers =[0, 1, 0, 3, 12, 0, 5]
result = []
for num in numbers:
    if num != 0:
        result.append(num)
for num in numbers:
    if num==0:
        result.append(num)
print(result)