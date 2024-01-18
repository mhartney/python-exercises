"""This program demonstrates use of the functions; 
replace(), upper(). It also prints string in reverse order."""

# Define string variable.
SENTENCE = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace the '!' character with a blank space ' ' and update string variable.
SENTENCE = SENTENCE.replace("!", " ")
print(f"\n1. Replace Characters:\n{SENTENCE}\n")

# Print the string in uppercase.
print(f"2. Print in Uppercase:\n{SENTENCE.upper()}\n")

# Print the SENTENCE in reverse.
print(f"3. Print in Reverse Order:\n{SENTENCE[::-1]}\n")
