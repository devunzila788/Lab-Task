def calculate_sum(*args):
    total = 0
    for num in args:
        total = total + num
    return total
result = calculate_sum(10, 20, 30, 40, 50)
print("Sum is:", result)