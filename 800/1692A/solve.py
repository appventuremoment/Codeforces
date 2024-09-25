for _ in range(int(input())):
    dist = list(map(int, input().split(' ')))
    timmy = dist[0]
    print(sorted(dist)[::-1].index(timmy))