row, col = map(int, input().split(' '))
for r in range(row):
    if r % 4 == 1:
        print('.' * (col - 1) + '#')
    elif r % 4 == 3:
        print('#' + '.' * (col - 1))
    else:
        print('#' * col)