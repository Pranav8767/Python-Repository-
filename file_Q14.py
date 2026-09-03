old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as f:
    data = f.read()

data = data.replace(old_word, new_word)

with open("student.txt", "w") as f:
    f.write(data)

print("Word replaced successfully.")