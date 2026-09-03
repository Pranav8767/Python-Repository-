with open("program.py", "r") as f:
    lines = f.readlines()

with open("without_comments.py", "w") as f:
    for line in lines:
        if not line.strip().startswith("#"):
            f.write(line)

print("Comments removed.")