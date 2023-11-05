"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_RATE_10 = 0.1
BONUS_RATE_15 = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = BONUS_RATE_10
    else:
        bonus_rate = BONUS_RATE_15
    bonus = bonus_rate * sales
    print(f'Bonus is: ${bonus}')
    sales = float(input("Enter sales: $"))
print("Goodbye...")

