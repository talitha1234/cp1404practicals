"""
Taxi simulator
Estimate: 30 mins
Actual: 235pm
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'C':
            if current_taxi:
                pass
            else:
                "You need to choose a taxi before you can drive"
        elif choice == 'D':
            pass
        else:
            print('Invalid option')

        print(f'${bill_to_date:,.2f}')
        choice = input(MENU)
    # <do final thing, if needed>


main()
