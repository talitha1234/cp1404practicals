"""
Score Menu
G Get a valid score (0-100)
P Print result
S Show stars
Q Quit

 """
import random

from score import determine_score_status

MENU = [f'G Get a valid score (0-100)\n'
        f'P Print result\n'
        f'S Show stars\n'
        f'Q Quit']


def main():
    """
    Score Menu
    G Get a valid score (0-100)
    P Print result
    S Show stars
    Q Quit

    """
    score = 0
    print(*MENU)
    choice = input(">").lower()
    while choice != 'q':
        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            status = determine_score_status(score)
            print("Result:", status)
        elif choice == 's':
            print_stars(int(score))
        else:
            print("Invalid choice")
        print(*MENU)
        choice = input(">").lower()
    random_score = random.randint(1, 100)
    print(f'Random score: {random_score}, Status: {determine_score_status(random_score)}')
    print("Bye.......")


def get_valid_score():
    """Get score in range of 1 to 100"""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Not a valid score.")
        score = input("Score: ")
    return score


def print_stars(length):
    """Print stars for length"""
    print('*' * length)


main()
