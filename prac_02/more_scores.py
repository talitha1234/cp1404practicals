import random


def main():
    number_of_scores = int(input("Number of scores to generate: "))

    with open('results', 'w') as out_file:
        for score in range(number_of_scores):
            score = random.randint(1, 100)

            result = determine_score_status(score)

            out_file.write(f'{score} is {result}\n')


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