import math
splitted = map(int, input().split(' '))
m, n, a = splitted

print(math.ceil(m / a) * math.ceil(n / a))
