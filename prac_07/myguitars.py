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
    guitars.sort()
    print(guitars)
