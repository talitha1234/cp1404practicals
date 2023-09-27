name = input("Name: ")
file_out = open('name.txt', 'w')
print(name, file=file_out)
file_out.close()

with open('name.txt', 'r') as file_in:
    text = file_in.read()
    print("Your name is", text)

with open("numbers.txt", 'w') as file_out:
    # print(17, 42, 400, sep='\n', file=file_out)
    print('{}\n{}\n{}'.format(17, 42, 400), file=file_out)
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(first_number + second_number)

with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
