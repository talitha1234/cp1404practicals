numbers = [3, 1, 4, 1, 5, 9, 2]


# numbers[0], result: 3
# numbers[-1], result: 2
# numbers[3], result: 1
# numbers[:-1] result: 3 1 4 1 5 9
# numbers[3:4] result: 1
# 5 in numbers: True
# 7 in numbers: False
# "3" in numbers: False
# numbers + [6, 5, 3]: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = 'ten'
print(numbers)  # to check value has changed can also check in debugger

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)  # to check value has changed can also check in debugger

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)
