from temperatures import convert_fahrenheit_to_celsius, convert_celsius_to_fahrenheit
import random


with open('temps_input.txt', 'r') as file_in:
    with open('temps_output.txt', 'w') as file_out:
        for line in file_in:
            celsius = convert_fahrenheit_to_celsius(int(line))  # convert input string to int
            print(f'{celsius}\n', file=file_out)


#TODO: GPS (Gopher Population Simulator) section