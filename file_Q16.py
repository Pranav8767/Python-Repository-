with open("student.txt", "r") as f:
    data = f.read()

with open("uppercase.txt", "w") as f:
    f.write(data.upper())

print("Uppercase file created.")