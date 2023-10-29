"""
Guitar.
Estimate: 20 mins, 6:27pm start
Actual: 12 mins, 6:39 finish
"""
import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        return datetime.date.today().year - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        return False
