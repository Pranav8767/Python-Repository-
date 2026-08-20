python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Priya", "Rohan", "Sneha", "Vikas"}

print("Students in both courses:", python_students & java_students)

print("Students only in Python:", python_students - java_students)
print("Students only in Java:", java_students - python_students)

print("Students enrolled in only one course:",
      python_students ^ java_students)