"""
Emails
Estimate: 30 minutes
Actual: 35 minutes
"""

email_to_name = {}

email = input("Email: ")
while email != '':
    # get name from email and capitalise first letters of name
    name = email[:email.index('@')].replace('.', ' ').title()

    # check name is correct
    choice = input(f"Is your name {name} (Y/n)?").upper()

    # the user does not press Enter or Y, then ask for their name.
    if choice != 'Y' and choice != '':
        name = input("Name: ").title()

    # add email and name to dictionary
    email_to_name[email] = name

    email = input("Email: ")

# loop through and print out
for email, name in email_to_name.items():
    print(f'{name} ({email})')






