friends, presents = int(input()), list(map(int, input().split(' ')))
ret = [0 for _ in range(friends)]
for x in range(friends): ret[presents[x] - 1] = str(x + 1)
print(' '.join(ret))