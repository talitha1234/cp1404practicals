"""
Silver Service Taxi
Estimate: 15 mins
Actual: 20 mins
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * fanciness
        print(self.price_per_km)

    def __str__(self):
        """Return string like Taxi but with Flagfall added"""
        return (f'{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, '
                f'${self.price_per_km}/km plus flagfall of ${self.flagfall:,.2f}')

    def get_fare(self):
        """Return the price for the fancy taxi trip."""
        return super().get_fare() + self.flagfall
