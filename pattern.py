"""This program uses a single for loop in combination
with an if-else statement to print the requested pattern."""

import random

def pattern(print_num):
    while print_num != 0:
        SIZE = random.randint(10, 50)
        COUNT = 0
        for i in range(0, SIZE):
            if i < (SIZE / 2):
                COUNT += 1
            else:
                COUNT -= 1
            print(COUNT * '*')
        print_num -= 1

print_num = int(input("How many times would you like to print the pattern? "))
pattern(print_num)