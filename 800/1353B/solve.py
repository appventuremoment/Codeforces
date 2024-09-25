for _ in range(int(input())):
    _, swaps = map(int, input().split(' '))
    a, b = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
    for _ in range(swaps):
        if a[a.index(min(a))] < b[b.index(max(b))]: a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
        else: break
    print(sum(a))