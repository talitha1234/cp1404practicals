# Basic list operations
numbers = []
for i in range(5):
    list_number = int(input("Number: "))
    numbers.append(list_number)
print(f"The first number is: {numbers[0]}")
print(f"The last number: {numbers[-1]}")
print(f"The smallest number: {min(numbers)}")
print(f"The largest number: {max(numbers)}")
print(f"The average of the numbers: {sum(numbers) / len(numbers)}")


# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
