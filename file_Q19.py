with open("attendance.txt", "r") as f:
    for line in f:
        roll, name, present, total = line.strip().split(",")

        percentage = (int(present) / int(total)) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print("Below 75%")