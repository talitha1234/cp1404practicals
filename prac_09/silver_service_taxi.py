"""
Silver Service Taxi
Estimate: 15 mins
Actual: 20 mins
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi class, inherits from Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        # checking price is correct
        # print(self.price_per_km)

    def __str__(self):
        """Return string like Taxi but with Flagfall added"""
        return f'{super().__str__()}, plus flagfall of ${self.flagfall:.2f}'

    def get_fare(self):
        """Return the price for the fancy taxi trip."""
        return super().get_fare() + self.flagfall
