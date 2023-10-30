"""
Guitar.
Estimate: 40 mins, start 7:50pm
Actual: 26 mins, finish 8:16pm
"""
from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != '':
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")

# statements used for testing without input
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars, 1):
    print(f'Guitar {i}: {guitar.name:>20} ({guitar.year}). worth ${guitar.cost:10,.2f}'
          f'{"(vintage)" if guitar.is_vintage() else ""}')
