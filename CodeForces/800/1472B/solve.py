for _ in range(int(input())):
    input()
    candies = list(map(int, input().split(' ')))
    ones, twos = candies.count(1), candies.count(2)
    if twos % 2 == 1:
        if ones >= 2 and ones % 2 == 0: print('YES')
        else: print('NO')
    else:
        if ones % 2 == 0: print('YES')
        else: print('NO')