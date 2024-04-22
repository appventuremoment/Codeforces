n, k, l, c, d, p, nl, np = map(int, input().split(' '))
print(min(c * d // n, k * l // (nl  * n), p // (np * n)))