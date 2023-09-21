"""
Score Menu
G Get a valid score (0-100)
P Print result
S Show stars
Q Quit

 """

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


def determine_score_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
