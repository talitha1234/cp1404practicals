""" Different ways to read files using """

# 1. Asks the user for their name, then opens a file called "name.txt" and writes that name to it.
name = input("Name: ")
file_out = open('name.txt', 'w')
print(name, file=file_out)
file_out.close()

# 2. Opens "name.txt" and reads the name (as above) then prints "Your name is ..."
with open('name.txt', 'r') as file_in:
    text = file_in.read()
    print("Your name is", text)

# 3. Opens "numbers.txt", reads only the first two numbers and adds them together then prints the result: 59
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())  # 1st line of file
    second_number = int(in_file.readline())  # 2nd line
    print(first_number + second_number)

# 4. Prints the total for all lines in numbers.txt or a file with any amount of numbers. 
with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)

