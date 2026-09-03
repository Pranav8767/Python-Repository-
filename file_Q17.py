with open("students.txt", "r") as f:
    next(f)

    students = []

    for line in f:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
print("\nHighest Marks:", highest[1], highest[2])

average = sum(s[2] for s in students) / len(students)
print("Average Marks:", average)

print("\nStudents scoring more than 80:")
for s in students:
    if s[2] > 80:
        print(s[1])