"""
Guitar Test
Estimate: 20 mins, 6:45pm start
Actual: 9 mins, 6:54pm finish
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(f'{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}')
another_guitar = Guitar("Another Guitar", 1973, 1500.35)
print(f'{another_guitar.name} get_age() - Expected 50. Got {another_guitar.get_age()}')
print(f'{guitar.name} is_vintage() - Expected True - got {guitar.is_vintage()}')
print(f'{another_guitar.name} is_vintage() - Expected False - got {another_guitar.is_vintage()}')
