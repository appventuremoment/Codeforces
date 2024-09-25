n, a, b = int(input()), int(input()), int(input())
if n == 1:
    if a == b: print(1)
    else: print(0)
    print(f"{a}:{b}")
else:
    print(max(0, n - a - b))
    results = [[0, 0] for _ in range(n)]
    round = 0
    while round < n and a > 0:
        a -= 1
        results[round][0] += 1
        round += 1

    if a > 0:
        results[0][0] += a

    if b > 0:
        if round == n:
            results[0][0] += 1
            results[1][0] -= 1
            results[1][1] += b
        else:
            while round < n and b > 0:
                b -= 1
                results[round][1] += 1
                round += 1
            if b > 0:
                results[n - 1][1] += b

    for x in results: print(":".join(list(map(str, x))))