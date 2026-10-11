numbers = [1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]
count =1
longest =1
for i in range(1, len(numbers)):
    if numbers[i]==numbers[i - 1]:
        count += 1
    else:
        count = 1

    if count>longest:
        longest=count
print(longest)