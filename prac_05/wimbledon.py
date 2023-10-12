"""
Word Occurrences
Estimate: 120 mins
Actual: roughly 2 or more hours split up over a few days
"""
filename = 'wimbledon.csv'


def main():
    """
    Displays the champions and how many times they have won.
    Display the countries of the champions in alphabetical order
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # read first line in file to skip and get rest of lines
        in_file.readline()
        lines = [line.strip().split(',') for line in in_file]

        champion_to_win_count = calculate_champion_to_win_count(lines)
        display_champion_to_win_count(champion_to_win_count)

        display_champion_countries(lines)


def display_champion_to_win_count(champion_to_win_count):
    """Displays champions using champion win count dictionary"""
    print("Wimbledon Champions")
    print("\n".join((f'{champion} {count}' for champion, count in champion_to_win_count.items())))


def calculate_champion_to_win_count(lines):
    """Champions and how many times they have won. (List of lists and dictionary)"""
    champions = [line[2] for line in lines]
    # count number of times they were champions
    #  dictionary
    champion_to_win_count = {}
    for champion in champions:
        # add the champion
        # get returns number of wins for champion or default to zero if no wins counted yet
        champion_to_win_count[champion] = champion_to_win_count.get(champion, 0) + 1
    return champion_to_win_count


def display_champion_countries(lines):
    """Displays champion country codes"""
    # the countries of the champions in alphabetical order
    # set to remove duplicates, sorted in ABC order join it all with spaces between
    countries = set(f'{line[1]}' for line in lines)
    champion_to_country_code = " ".join(sorted(countries))
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(champion_to_country_code)


main()
