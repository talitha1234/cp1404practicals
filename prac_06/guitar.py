"""
Guitar.
Estimate: 20 mins, 6:27pm start
Actual: 15 mins, 6:39 finish, + 3 mins
"""
import datetime

VINTAGE_AGE = 50


class Guitar:
    """"Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a car object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of data in car."""
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        """Return the age of a guitar."""
        return datetime.date.today().year - self.year

    def is_vintage(self):
        """Return True if guitar is older than 50 years"""
        return self.get_age() > VINTAGE_AGE

