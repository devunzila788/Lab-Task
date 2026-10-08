my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

total = 0

for number in my_list:
    total = total + number

average = total / len(my_list)

print("Sum:", total)
print("Average:", average)