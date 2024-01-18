"""This program uses two different string building techniques.
It takes an input sentence from user and then gives it a new unique
format by building two new sentences."""

# Get input sentence from user.
print("\n===Format String===")
user_input = input("Enter Text: ")

# Use loop to run over each letter in input string.
NEW_STRING_1 = ""
COUNT = 0
while COUNT < len(user_input):
    # Use count to go through string index.
    for i in user_input:
        if COUNT % 2 == 0:
            # Capitalise letter if even.
            NEW_STRING_1 += i.upper()
        else:
            NEW_STRING_1 += i.lower()
        COUNT += 1

# Print every other word of input string in capitals.
string_list = user_input.split()
new_list = []
COUNT = 0
while COUNT < len(string_list):
    for i in string_list:
        if COUNT % 2 == 1:
            # Capitalise word if odd and add to new list.
            new_list.append(str(i).upper())
        else:
            new_list.append(str(i).lower())
        COUNT += 1
NEW_STRING_2 = " ".join(new_list)

# Print results for both strings.
print(f"\nMethod 1:\n{NEW_STRING_1}\n{NEW_STRING_2}\n")

# Above tasks using list comprehension.
# Task 1.
string_list_1 = [i.upper() if x % 2 == 0 else i.lower() for x, i in enumerate(user_input)]
NEW_STRING_3 = ''.join(string_list_1)

# Task 2.
new_list = [i.upper() if x % 2 == 0 else i.lower() for x, i in enumerate(user_input.split())]
NEW_STRING_4 = ' '.join(new_list)

# Print results.
print(f"Method 2:\n{NEW_STRING_3}\n{NEW_STRING_4}\n")
