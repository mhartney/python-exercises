"""This program strips the string so that it spells Superman."""

# Define variable.
HERO = "$$$Superman$$$"

# Method 1: Strip '$' character and update varibale.
HERO = HERO.strip("$")
print(f"Method 1: {HERO}")

# Method 2: Strip '$' character directly from string.
HERO = "$$$Superman$$$".strip("$")
print(f"Method 2: {HERO}")
