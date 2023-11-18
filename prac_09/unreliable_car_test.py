"""
Unreliable Car Test
Estimate: 10 mins
Actual: 15 mins
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable car"""
    old_car = UnreliableCar("old car", 50, 100)
    print("Before attempt drive")
    print(old_car)
    print("After attempt drive")
    old_car.drive(20)
    print(old_car)

    other_old_car = UnreliableCar("other_old_car", 50, 1)
    print("Before attempt drive")
    print(other_old_car)
    other_old_car.drive(20)
    print("After attempt drive")
    print(other_old_car)

    # # check inherited method still works
    # old_car.add_fuel(100)
    # print(old_car)


main()
