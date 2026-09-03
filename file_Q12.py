with open("student.txt", "r") as f:
    data = f.read().lower()

words = data.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)