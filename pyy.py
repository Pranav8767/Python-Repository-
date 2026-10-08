user_string = input("Enter a string: ")
vowels_count = 0
consonants_count = 0
digits_count = 0
spaces_count = 0
special_count = 0
vowels = "aeiou"
for char in user_string:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    elif char.isdigit(): 
        digits_count += 1
    elif char.isspace(): 
        spaces_count += 1
    else: 
        special_count += 1
print("\nAnalysis Results:")
print(f"Vowels:             {vowels_count}")
print(f"Consonants:         {consonants_count}")
print(f"Digits:             {digits_count}")
print(f"Special Characters: {special_count}")

