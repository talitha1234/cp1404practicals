"""
Data file -> lists program
Displays data from subjects and demonstrates process with print statements and returns to main with list
"""

FILENAME = "subject_data.txt"


def main():
    """Displays data from subjects and demonstrates process with print statements and returns to main with list"""
    data = get_data()
    print(data)
    display_subject_details(data)


def display_subject_details(data):
    """Displays subject details from data"""
    for point in data:
        print(f'{point[0]} is taught by {point[1]} and has {point[2]} students')


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


main()
