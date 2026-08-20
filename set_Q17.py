morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Priya", "Sneha", "Rohan", "Vikas"}

print("Present in both:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("Present in at least one session:", morning | afternoon)