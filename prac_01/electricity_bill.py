CENTS_TO_DOLLAR_RATIO = 1/100
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# price_per_kwh_cents = float(input('Enter cents per kWh: '))
tariff_choice = int(input("Which tariff? 11 or 31: "))
daily_use_kwh = float(input('Enter daily use in kWh: '))
number_of_days = float(input('Enter number of billing days: '))

if tariff_choice == 11:
    price_per_kwh_cents = TARIFF_11
elif tariff_choice == 31:
    price_per_kwh_cents = TARIFF_31

# estimated_bill_dollars = price_per_kwh_cents*daily_use_kwh*number_of_days*CENTS_TO_DOLLAR_RATIO

estimated_bill_dollars = price_per_kwh_cents*daily_use_kwh*number_of_days

print(f'Estimated bill: ${estimated_bill_dollars:.2f}')


