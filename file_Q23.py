with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()

with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Files are identical.")
else:
    print("Files are different.")

    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("First difference at line:", i + 1)
            break