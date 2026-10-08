name = input("Enter your name: ")
age = int(input("Enter your age: "))
program = input("Enter your program: ")
marks = float(input("Enter your marks: "))

student = (name, age, program, marks)

print("\nStudent Information:")
print("Name:", student[0])
print("Age:", student[1])
print("Program:", student[2])
print("Marks:", student[3])