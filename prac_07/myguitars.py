import csv
from prac_07.guitar import Guitar

# newline handles newline character when file is read
with open("guitars.csv", 'r', newline='') as in_file:
    # format of file:Name,Year,Cost
    # make csv object of file; returned object is iterator
    reader = csv.reader(in_file)
    guitars = []
    for row in reader:
        guitar = Guitar(row[0], int(row[1]), float(row[2]))
        guitars.append(guitar)

    print("Want to add a guitar?")
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, int(year), float(cost)))
        name = input("Name: ")

    guitars.sort()
    # Print to check guitars are sorted by year
    # print(guitars)



with open("guitars.csv", 'w') as out_file:
    for guitar in guitars:
        guitar_string = f'{guitar.name},{guitar.year},{guitar.cost}\n'
        out_file.write(guitar_string)
