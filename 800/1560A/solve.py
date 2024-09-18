polycarp = [x for x in range(1, 2000) if x % 3 != 0 and str(x)[-1] != '3']
for _ in range(int(input())): print(polycarp[int(input()) - 1])