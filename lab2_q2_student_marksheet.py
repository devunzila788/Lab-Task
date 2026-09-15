# Lab2 - Advanced Student Marksheet
# Written in PyCharm

print("==================================================")
print("       ADVANCED STUDENT MARKSHEET")
print("==================================================")

name = input("Enter Student Name      : ")
roll_no = input("Enter Roll Number       : ")

print()
print("Enter marks for 5 subjects (out of 100):")
m1 = float(input("  Subject 1 marks: "))
m2 = float(input("  Subject 2 marks: "))
m3 = float(input("  Subject 3 marks: "))
m4 = float(input("  Subject 4 marks: "))
m5 = float(input("  Subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

# If any subject is below 40 -> Fail
if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40:
    grade = "F"
    result = "Fail"
else:
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

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

print()
print("==================================================")
print("              FINAL MARKSHEET")
print("==================================================")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("--------------------------------------------------")
print("Subject Marks:")
print("  Subject 1  :", m1)
print("  Subject 2  :", m2)
print("  Subject 3  :", m3)
print("  Subject 4  :", m4)
print("  Subject 5  :", m5)
print("--------------------------------------------------")
print("Total Marks  :", total, "/ 500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Result       :", result)
print("==================================================")
