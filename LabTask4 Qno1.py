my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

smallest = my_list[0]

for number in my_list:
    if number < smallest:
        smallest = number

print("Smallest number:", smallest)