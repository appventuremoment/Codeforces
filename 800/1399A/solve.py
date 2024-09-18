for _ in range(int(input())):
    leng = int(input())
    numbers = sorted(list(map(int, input().split(' '))))
    if leng == 1: print('YES'); continue
    if len(['no.' for x in range(1, len(numbers)) if numbers[x] - numbers[x - 1] > 1]) > 0: print('NO')
    else: print('YES')