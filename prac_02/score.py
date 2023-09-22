"""
Determine grade score status of user score and randomly generated score
Print grade and status
"""
import random


def main():
    """ Determine score status of user score and randomly generated score """
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(f'Grade {score} Status: {status}')
    random_score = random.randint(1, 100)
    status_random_score = determine_score_status(random_score)
    print(f'Grade {random_score} Status: {status_random_score}')


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


if __name__ == "__main__":
    main()
