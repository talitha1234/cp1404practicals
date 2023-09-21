name = input("Name: ")

choice = input('(H)ello'
               '\n(G)oodbye'
               '\n(Q)uit\n').upper()
while choice != 'Q':

    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
    choice = input('(H)ello'
                   '\n(G)oodbye'
                   '\n(Q)uit\n').upper()

print('Bye...')
