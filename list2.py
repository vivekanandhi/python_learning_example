numbers = [1,2,3,4,5,6,7,7,8,8,9,0,2,3]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)