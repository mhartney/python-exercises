"""This program reads information from a text file, formats and then prints.
The text file is a list of names and birthdates."""

# Input text file.
DOB_FILE = "DOB.txt"

# Try statement checks if file is missing.
try:
    # Open file and read lines into variable.
    with open(DOB_FILE, 'r', encoding="utf-8-sig") as file:
        lines = file.readlines()
    file.close()

    # Extract information to format.
    FILE_NAMES = ''
    FILE_DOBS = ''
    # Split text by delimiter ' ' (blank space).
    for line in lines:
        get_info = line.split(' ')
        # Add information from lines list into string variables.
        FILE_NAMES += ''.join(f"{get_info[0]} {get_info[1]} \n")
        FILE_DOBS += ' '.join(get_info[2:5])

    # Format text and print.
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    name_title = f"\n{BOLD_START}Name{BOLD_END}\n"
    dob_title = f"\n{BOLD_START}Birthdate{BOLD_END}\n"
    formatted_contents = f"{name_title}{FILE_NAMES}{dob_title}{FILE_DOBS}"
    # Print before and after.
    print(f"\nOriginal:\n\n{lines}")
    print(f"\nFormatted:\n{formatted_contents}")

except FileNotFoundError as error:
    print(f"{error}: make sure the input file is in your current working directory.")
