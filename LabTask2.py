hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    total_pay = hours * rate
else:
    overtime = hours - 40
    total_pay = (40 * rate) + (overtime * rate * 1.5)

print("Total pay:", total_pay)