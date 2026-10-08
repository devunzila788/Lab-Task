marks = []

for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 500 * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if all(mark >= 40 for mark in marks):
    result = "Pass"
else:
    result = "Fail"

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)