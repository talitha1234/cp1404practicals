"""
Guitar Test
Estimate: 20 mins, 6:45pm start
Actual: 9 mins, 6:54pm finish
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(f'{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}')
another_guitar = Guitar("Another Guitar", 2020, 1500.35)
print(f'{another_guitar.name} get_age() - Expected 3. Got {another_guitar.get_age()}')
