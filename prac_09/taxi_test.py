"""
Taxi Test
Estimate: 20 mins
Actual: 15 mins
"""
from prac_09.taxi import Taxi


def main():
    """Test Taxi Class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f'{my_taxi} current fare total: {my_taxi.get_fare()}')
    my_taxi.start_fare()
    # Check fare distance has been cleared
    # print(my_taxi.current_fare_distance)
    my_taxi.drive(100)
    print(f'{my_taxi} current fare total: {my_taxi.get_fare()}')


main()
