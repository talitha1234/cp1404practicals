import random

STARTING_POPULATION = 1000
MINIMUM_PERCENTAGE_BORN = .1
MAXIMUM_PERCENTAGE_BORN = .2
MINIMUM_PERCENTAGE_DEAD = .05
MAXIMUM_PERCENTAGE_DEAD = .25
NUMBER_OF_YEARS = 10

print(' Welcome to the Gopher Population Simulator!')
print(f'Starting population: {STARTING_POPULATION}')
current_population = STARTING_POPULATION

for year in range(NUMBER_OF_YEARS):
    print(f'Year {year}\n')
    number_born = int(random.uniform(MINIMUM_PERCENTAGE_BORN, MAXIMUM_PERCENTAGE_BORN) * current_population)
    number_died = int(random.uniform(MINIMUM_PERCENTAGE_DEAD, MAXIMUM_PERCENTAGE_DEAD) * current_population)
    print(f'{number_born} gophers were born. {number_died} died.', sep='')
    current_population = current_population + number_born - number_died
    print(f'Population: {current_population}')
