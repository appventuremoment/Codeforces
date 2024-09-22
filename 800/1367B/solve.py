for _ in range(int(input())):
    input()
    issues = (lambda listofnum: [listofnum[x] for x in range(len(listofnum)) if listofnum[x] % 2 != x % 2])(list(map(int, input().split(' '))))
    odds, evens = len([x for x in issues if x % 2 == 1]), len([x for x in issues if x % 2 == 0])
    if odds == evens: print(evens)
    else: print(-1)