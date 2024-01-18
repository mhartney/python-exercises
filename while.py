"""This program continuously asks the user for a number.
It then calculates the average of the numbers entered,
after -1 is entered."""

# User input is captured in a list.
user_numbers = []
print("\n" + ('+' * 30) + "\n")
EXIT_ENTERED = False
while not EXIT_ENTERED:
    user_num = input("Enter Number: ")
    if user_num.isalpha():
        print(f"\nType numbers only. You wrote '{user_num}' e.g Enter Number: 5\n")
        continue
    user_num = int(user_num)
    if user_num == -1:
        EXIT_ENTERED = True
    else:
        user_numbers.append(user_num)
print("\n" + ('+' * 30) + "\n")

# Sum of numbers in list calculated.
TOTAL_SUM = 0
for num in user_numbers:
    TOTAL_SUM += num

# Calculate arithemtic mean or average.
average = TOTAL_SUM / len(user_numbers)
print(f"""Arithmetic Mean:
Average is the total sum of numbers ({TOTAL_SUM}), 
divided by number of numbers entered ({len(user_numbers)}).\n""")

# Print results.
print("Numbers Entered:")
COUNT = 0
for COUNT, num in enumerate(user_numbers, 1):
    print(f"{COUNT}. {num}")

print(f"""Total Sum = {TOTAL_SUM}

Your Results:
{TOTAL_SUM} % {len(user_numbers)}
Average = {round(average,2)}
""")
