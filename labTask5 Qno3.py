employees = []

for i in range(3):
    print("\nEnter information for Employee", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\n===== EMPLOYEE INFORMATION =====")

for employee in employees:
    print("Name:", employee[0])
    print("Age:", employee[1])
    print("Salary:", employee[2])
    print("----------------------")