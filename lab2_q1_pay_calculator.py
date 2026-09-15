# Lab2 - Pay Calculator
# Written in PyCharm

print("========================================")
print("   Employee Pay Calculator")
print("========================================")

hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    total_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    total_pay = regular_pay + overtime_pay

print("----------------------------------------")
print("Hours Worked :", hours)
print("Hourly Rate  :", rate)
print("Total Pay    :", round(total_pay, 2))
print("========================================")
