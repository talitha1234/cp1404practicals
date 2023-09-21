password = input("Password: ")
while len(password) < 5:
    print("Invalid password. Must be greater than 5 characters.")
    password = input("Password: ")
print(len(password) * '*')
