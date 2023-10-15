"""
Word Occurrences
Estimate: 120 mins
Actual: 3 or 4 hours
"""
FILENAME = 'wimbledon.csv'


def main():
    """
    Displays the champions and how many times they have won.
    Display the countries of the champions in alphabetical order
    """

    records = get_records(FILENAME)
    champion_to_win_count, countries = return_evaluated_records(records)
    display_champion_to_win_count(champion_to_win_count)
    display_champion_countries(countries)


def get_records(lines):
    """Gets the lines from a file and formats it so that the data can be read"""
    with open(lines, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        # get lines and separate into list of parts list
        records = [line.strip().split(',') for line in in_file]
    return records


def return_evaluated_records(records):
    """Evaluate the records and returns champions with win count and the list of countries that have won in
    alphabetical order"""
    countries_and_champions = [(line[1], line[2]) for line in records]
    countries = []
    champion_to_win_count = {}
    for country, champion in countries_and_champions:
        champion_to_win_count[champion] = champion_to_win_count.get(champion, 0) + 1
        countries.append(country)

    return champion_to_win_count, (sorted(set(countries)))


def display_champion_to_win_count(champion_to_win_count):
    """Displays champions using champion win count dictionary"""
    print("Wimbledon Champions")
    print("\n".join((f'{champion} {count}' for champion, count in champion_to_win_count.items())))


def display_champion_countries(countries):
    """Displays champion country codes using list of unique country codes"""
    # the countries of the champions in alphabetical order
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(*countries)


main()
