with open("student.txt", "r") as f:
    data = f.read()

words = data.split()

print("Total words:", len(words))