name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subject1 = float(input("Enter marks for English: "))
subject2 = float(input("Enter marks for Math: "))
subject3 = float(input("Enter marks for Computer: "))
subject4 = float(input("Enter marks for Physics: "))
subject5 = float(input("Enter marks for Chemistry: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
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

if (subject1 < 40 or subject2 < 40 or subject3 < 40 or
    subject4 < 40 or subject5 < 40):
    result = "Fail"
else:
    result = "Pass"

print("\n========== STUDENT MARKSHEET ==========")
print("Name       :", name)
print("Roll No    :", roll_no)
print("---------------------------------------")
print("English    :", subject1)
print("Math       :", subject2)
print("Computer   :", subject3)
print("Physics    :", subject4)
print("Chemistry  :", subject5)
print("---------------------------------------")
print("Total Marks:", total, "/ 500")
print("Percentage :", percentage, "%")
print("Grade      :", grade)
print("Result     :", result)
print("=======================================")
