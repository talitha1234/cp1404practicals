"""
Quick Pick program
Prints a number of lines with 6 random numbers
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Prints a number of lines with sets of random numbers"""
    number_of_lines = int(input("Number of quick picks: "))  # quick pick is a list of 6 numbers per line
    # check for valid input not less than zero

    while number_of_lines < 0:
        print("Can't have negative quick picks.")
        number_of_lines = int(input("Number of quick picks: "))  # quick pick is a list of 6 numbers per line

    for line in range(number_of_lines):
        numbers = []
        for number in range(NUMBERS_PER_LINE):  # generate line with 6 randoms numbers between 1 and 45
            number = random.randint(MINIMUM, MAXIMUM)
            while number in numbers:  # add number after checking it's not already in numbers
                number = random.randint(MINIMUM, MAXIMUM)
            numbers.append(number)  # remember randint is inclusive end unlike range function
        numbers.sort()  # display in ascending order

        print(" ".join((f'{number:2}' for number in numbers)))


main()
