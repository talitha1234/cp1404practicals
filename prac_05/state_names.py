"""
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern "
                "Territory", "WA": "Western Australia", "ACT": "Australian"
                " Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# .join to iterate over generator object to print each line
# print('\n'.join(f'{state_code:3} is {state_name}' for state_code, state_name in CODE_TO_NAME.items()))

# print using for loop
for state_code, state_name in CODE_TO_NAME.items():
    print(f'{state_code:3} is {state_name}')

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
