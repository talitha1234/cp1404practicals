import math


def main():
    choice = input('Show the (E)VEN numbers from x to y'
                   '\nShow the (O)DD numbers from x to y'
                   '\nShow the (S)QUARES from x to y'
                   '\n(Q)uit the program'
                   '\n').upper()

    while choice != 'Q':
        if choice == "E":
            x, y = get_min_max()
            numbers = get_even_numbers(x, y)
            print(numbers)
        elif choice == 'O':
            x, y = get_min_max()
            numbers = get_odd_numbers(x, y)
            print(numbers)
        elif choice == 'S':
            x, y = get_min_max()
            numbers = generate_square_numbers(x, y)
            print(numbers)
        else:
            print("Invalid Choice")
        choice = input('Show the (E)VEN numbers from x to y'
                       f'\nShow the (O)DD numbers from x to y'
                       f'\nShow the (S)QUARES from x to y'
                       f'\n(Q)uit the program'
                       f'\n').upper()
    print("Bye")


def get_even_numbers(x, y):
    numbers = []
    if x % 2 == 1:
        x = x + 1
    for number in range(x, y + 1, 2):
        numbers.append(number)
    return numbers


def get_odd_numbers(x, y):
    numbers = []
    if x % 2 == 0:
        x = x + 1
    for number in range(x, y + 1, 2):
        numbers.append(number)
    return numbers


def generate_square_numbers(x, y):
    numbers = []
    for number in range(x, y + 1):
        square_root = math.sqrt(number)
        square_root_int = int(square_root)
        if square_root == square_root_int:
            numbers.append(number)
    return numbers


def get_min_max():
    x = int(input("Choose lower value for x: "))
    y = int(input("Choose lower value for y: "))
    return x, y


main()
