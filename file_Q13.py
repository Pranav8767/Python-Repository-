word = input("Enter word to search: ")
count = 0
lines_found = []

with open("student.txt", "r") as f:
    for line_no, line in enumerate(f, start=1):
        occurrences = line.lower().split().count(word.lower())

        if occurrences > 0:
            count += occurrences
            lines_found.append(line_no)

print("Occurrences:", count)
print("Line numbers:", lines_found)