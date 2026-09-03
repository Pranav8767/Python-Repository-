def display_employees(employees):
    for e in employees:
        print(e)


def highest_paid(employees):
    return max(employees, key=lambda x: x[3])


def average_salary(employees):
    return sum(e[3] for e in employees) / len(employees)


def above_salary(employees, salary):
    for e in employees:
        if e[3] > salary:
            print(e)


employees = [
    (101, "Amit", "IT", 50000),
    (102, "Priya", "HR", 60000),
    (103, "Rahul", "Sales", 45000)
]

print("All Employees:")
display_employees(employees)

print("\nHighest Paid:")
print(highest_paid(employees))

print("\nAverage Salary:")
print(average_salary(employees))

print("\nEmployees earning above 48000:")
above_salary(employees, 48000)