numbers = []

for i in range(1, 11):
    number = int(input("Enter number " + str(i) + ": "))
    numbers.append(number)

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nSum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)