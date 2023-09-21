for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()

n = int(input("Number of stars: "))
for i in range(0, n):
    print('*', end="")
print()


for stars_per_line in range(0, n + 1):
    print(f'*' * stars_per_line)

