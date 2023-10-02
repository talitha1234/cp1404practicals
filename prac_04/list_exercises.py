AMOUNT_OF_NUMBERS = 5
numbers = []
for number in range(AMOUNT_OF_NUMBERS):
    list_number = int(input("Number: "))
    numbers.append(list_number)
print(f"The first number is: {numbers[0]}")
print(f"The last number: {numbers[-1]}")
print(f"The smallest number: {min(numbers)}")
print(f"The largest number: {max(numbers)}")
print(f"The average of the numbers: {sum(numbers) / len(numbers)}")
