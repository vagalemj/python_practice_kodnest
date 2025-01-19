r = 5
c = 10

# Rectangle pattern
for i in range(r):
    for j in range(c):
        print('*', end='')
    print()

print()

# left Triangle pattern
for i in range(r):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print()

# down left Triangle pattern
for i in range(r):
    for j in range(i, r):
        print('*', end=' ')
    print()

print()

# right arrow Triangle pattern
for i in range(r):
    for j in range(i + 1):
        print('*', end=' ')
    print()
for i in range(r):
    for j in range(i, r - 1):
        print('*', end=' ')
    print()

print()

# butterfly pattern

for i in range(r):
    for j in range(i + 1):
        print('*', end='')
    for j in range(i, r - 1):
        print(' ', end='')
    for j in range(i, r - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(r):
    for j in range(i, r - 1):
        print('*', end='')
    for j in range(i + 1):
        print(' ', end='')
    for j in range(i + 1):
        print(' ', end='')
    for j in range(i, r - 1):
        print('*', end='')
    print()

# Diamond pattern

for i in range(r):
    for j in range(i, r):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(1, r):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(i, r - 1):
        print('*', end=' ')
    for j in range(i, r):
        print('*', end=' ')
    print()


