with open("student.txt", "r") as f:
    data = f.read()

words = data.split()

longest = max(words, key=len)

print("Longest word:", longest)