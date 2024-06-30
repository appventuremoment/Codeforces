import math
m, n, a = list(map(int, input().split(' ')))
print(math.ceil(m / a) * math.ceil(n / a))
