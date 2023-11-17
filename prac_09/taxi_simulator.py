"""
Taxi simulator
Estimate: 30 mins
Actual: 70 mins
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = 'q)uit, c)hoose taxi, d)rive\n>>> '


def main():
    """Taxi simulator with drive and choose taxi options"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'C':
            current_taxi = get_current_taxi(current_taxi, taxis)
        elif choice == 'D':
            fare = drive_current_taxi(current_taxi)
            bill_to_date += fare
        else:
            print('Invalid option')
        print(f'Bill to date: ${bill_to_date:,.2f}')
        choice = input(MENU).upper()
    print(f"Total trip cost: {bill_to_date:,.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_current_taxi(current_taxi):
    """Drive current taxi object if there is one"""
    if current_taxi:
        return get_drive_fare(current_taxi)
    else:
        print("You need to choose a taxi before you can drive")
        return 0


def get_drive_fare(current_taxi):
    """Get distance for fare"""
    distance = float(input("Drive how far? "))
    current_taxi.drive(distance)
    print(f'Your {current_taxi.name} trip cost you ${current_taxi.get_fare():,.2f}')
    return current_taxi.get_fare()


def get_current_taxi(current_taxi, taxis):
    """Get a valid taxi choice from list displayed"""
    display_taxis(taxis)
    is_valid_taxi_number = False
    while not is_valid_taxi_number:
        number_choice = input("Choose taxi: ")
        try:
            current_taxi = taxis[int(number_choice)]
            is_valid_taxi_number = True
        except ValueError:
            print("Invalid taxi choice")
        except IndexError:
            print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    """Display Taxis starting at 0"""
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


main()
