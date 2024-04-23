def solve(n, k):
    for _ in range(k):
        if n % 10 == 0: n //= 10
        else: n -= 1
    return n

print((lambda number, times: solve(number, times))(*map(int, input().split(' '))))