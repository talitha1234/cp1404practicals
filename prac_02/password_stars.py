"""Get password and print asterisks"""


def main():
    """Get password and print asterisks"""
    password = get_password()
    prints_asterisks(password)


def prints_asterisks(password):
    """Print asterisks"""
    print(len(password) * '*')


def get_password():
    """Get password from user"""
    password = input("Password: ")
    while len(password) < 5:
        print("Invalid password. Must be greater than 4 characters.")
        password = input("Password: ")
    return password


main()
