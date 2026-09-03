deposit = 0
withdrawal = 0
largest = 0
balance = 0

with open("transactions.txt", "r") as f:
    for line in f:
        typ, amount = line.strip().split(",")
        amount = int(amount)

        if typ == "D":
            deposit += amount
            balance += amount
        elif typ == "W":
            withdrawal += amount
            balance -= amount

        largest = max(largest, amount)

print("Total Deposits:", deposit)
print("Total Withdrawals:", withdrawal)
print("Final Balance:", balance)
print("Largest Transaction:", largest)