"""
Unreliable Car - Uses Car Class
Estimate: 15 mins
Actual: 15 mins
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name: str, fuel: float, reliability: float):
        """Construct unreliable car"""
        super().__init__(reliability)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        """Drive car if working"""
        if random.randint(0, 100) < self.reliability:
            print("Car started")
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            print("Car didn't start")
        return distance
