"""
Starter code for cumulative total income program.
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes)


def print_report(incomes):
    """Print cumulative income for number of incomes and corresponding number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    month = 0
    for month, income in enumerate(incomes, 1):  # enumerates over incomes and number of months
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
