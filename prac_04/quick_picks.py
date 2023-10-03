# get number of quick picks
# for number of quick picks
#   generate line with 6 randoms numbers between 1 and 45
# get rid of repeat numbers
# display in ascending order
# format align numbers
import random
NUMBERS_PER_LINE = 6

number_of_lines = int(input("Number of quick picks: "))  # quick pick is a list of 6 numbers per line
for line in range(number_of_lines):
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:  # generate line with 6 randoms numbers between 1 and 45
        numbers.append(random.randint(1, 45))
        if numbers[-1] in numbers[0:-1]:  # get rid of repeat numbers
            numbers.remove(numbers[-1])
    numbers.sort()  # display in ascending order
    for number in numbers:
        print(f"{number:>3}", end="")  # format align numbers
    print()


