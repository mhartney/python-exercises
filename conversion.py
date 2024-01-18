"""This program declares 4 different variables, then changes their type. 
It also shows the new converted variable being used in an example."""

# Declare the following variables.
NUM1 = 99.23
NUM2 = 23
NUM3 = 150
STRING1 = "100"

# Convert num1 variable from float to integer.
NUM1 = int(NUM1)
print("\nFloat to integer -")
print(f"Variable 1: {NUM1}")
print(f"Example. Variable x 2 = {NUM1 * 2}\n")

# Convert num2 variable from integer to float.
NUM2 = float(NUM2)
print("Integer to float -")
print(f"Variable 2: {NUM2}")
print(f"Example. Variable + 0.5 = {NUM2 + 0.5}\n")

# Convert num 3 from integer to string.
NUM3 = str(NUM3)
print("Integer to string -")
print(f"Variable 3: {NUM3}")
print(f"Example. Variable x 3 = {NUM3 * 3}\n")

# Convert string1 variable from string to integer.
STRING1 = int(STRING1)
print("String to integer -")
print(f"Variable 4: {STRING1}")
print(f"Example. Variable x 5 = {STRING1 * 5}\n")
