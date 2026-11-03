def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
employee_info(name="ibad", age=28, salary=60000, department="cs")