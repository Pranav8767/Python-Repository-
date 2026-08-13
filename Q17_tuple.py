t = (25,56,64,78,90)

largest = t[0]
smallest = t[0]

for n in t:
    if n > largest:
        largest = n
    elif n < smallest:
        smallest = n

print("Largest element:", largest)
print("Smallest element:", smallest)