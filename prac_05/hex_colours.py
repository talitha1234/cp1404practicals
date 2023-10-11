"""Colour name keys in a dictionary with hex code values"""

COLOUR_TO_CODE = {'PASTELPINK': '#dea5a4', 'FRENCHPINK': '#fd6c9e',
                  'LIGHTPINK': '#ffb6c1', 'MIMIPINK': '#ffdae9',
                  'MOUNTBATTENPINK': '#997a8d', 'NADESHIKOPINK': '#f6adc6',
                  'BABYPINK': '#f4c2c2', 'BAKER-MILLERPINK': '#ff91af',
                  'BRINKPINK': '#fb607f', 'CANDYPINK': '#e4717a'}
print(COLOUR_TO_CODE)
print('\n'.join(f'{colour_name:20} is {colour_code}' for colour_name, colour_code in COLOUR_TO_CODE.items()))

colour_name = input("Enter a pink colour: ").upper()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Is that pink?")

    colour_name = input("Enter pink colour: ").upper()
