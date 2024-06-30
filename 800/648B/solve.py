legs = int(input())
parts = sorted(list(map(int, input().split(' '))))
for a, b in zip(parts[:legs], parts[legs:][::-1]): print(a, b)