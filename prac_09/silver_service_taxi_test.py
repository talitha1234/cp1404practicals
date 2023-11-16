"""
Silver Service Taxi Tests
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test silver service taxi class"""
    fancy_taxi = SilverServiceTaxi(fanciness=2, name="Hummer", fuel=100)
    print(fancy_taxi)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(f'The current fare is ${fancy_taxi.get_fare():,.2f}')


main()
