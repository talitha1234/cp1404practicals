"""Get password and print asterisks"""

PASSWORD_MIN_LENGTH = 5


def main():
    """Get password and print asterisks"""
    password = get_password(PASSWORD_MIN_LENGTH)
    prints_asterisks(password)


def prints_asterisks(password):
    """Print asterisks"""
    print(len(password) * '*')


def get_password(min_length):
    """Get password from user"""
    password = input("Password: ")
    while len(password) < min_length:
        print(f"Invalid password. Must be at least {min_length} characters.")
        password = input("Password: ")
    return password


main()
