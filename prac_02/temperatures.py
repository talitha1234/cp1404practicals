"""
Get temperature and convert temperatures celsius and fahrenheit

C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit

"""
MENU = ["C - Convert Celsius to Fahrenheit\n"
        "F - Convert Fahrenheit to Celsius\n"
        "Q - Quit\n"]


def main():
    """Convert temperatures celsius and fahrenheit"""
    print(*MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_fahrenheit_to_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        print(*MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def convert_fahrenheit_to_celsius():
    """Convert convert fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit():
    """Convert celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    return celsius * 9.0 / 5 + 32


main()
