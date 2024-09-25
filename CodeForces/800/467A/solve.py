counter = 0
for _ in range(int(input())): counter += (lambda occ, cap: cap - occ >= 2 and 1 or 0)(*map(int, input().split(' ')))
print(counter)