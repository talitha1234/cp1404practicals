"""
Get temperature and convert temperatures celsius and fahrenheit

C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit

"""
MENU = ("C - Convert Celsius to Fahrenheit\n"
        "F - Convert Fahrenheit to Celsius\n"
        "Q - Quit\n")


def main():
    """Convert temperatures celsius and fahrenheit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""

    return celsius * 9.0 / 5 + 32


if __name__ == "__main__":
    main()

