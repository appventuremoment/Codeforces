# print((lambda n, k: [k % (n // 2)] )(*map(int, input().split(' '))))

# list(range(1 + min(int(k // (n / 2)), 1), n + 1, 2))

n, k = 10, 2
for n in range(1, 10):
    for k in range(1, n + 1):
        print((n, k))
        print(list(range(1 + min(int(k // (n / 2)), 1), n + 1, 2)))