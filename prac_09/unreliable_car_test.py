"""
Unreliable Car Test
Estimate: 10 mins
Actual: 15 mins
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable car"""
    old_car = UnreliableCar("old car", 50, 50)
    print(old_car)
    old_car.drive(20)
    print(old_car)
    # check inherited method still works
    old_car.add_fuel(100)
    print(old_car)


main()
