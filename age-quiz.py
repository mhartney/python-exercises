"""This program asks the user to enter their age and outputs a response."""

# Accept only numerical input from user.
ATTEMPTS = 0
while True:
    age = input("\nEnter Age: ")
    if age.isdecimal():
        print("\n")
        break
    print("\nError: Type your age in numbers. E.g Enter Age: 28")
    ATTEMPTS += 1
    if ATTEMPTS == 4:
        print("\nYou have tried 4 times now! Just type two numbers.")

# Output response depending on age given.
age = int(age)
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill!")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")
print("\n")
