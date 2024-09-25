for _ in range(int(input())):
    x, y, n = map(int, input().split(' '))
    temp = n % x
    if temp >= y: print(n - (temp - y))
    else: print(n - temp - (x - y))