def genMatrix(n, ivx, ivy, iv):
    elements = []
    for x in range(n):
        for y in range(n):
            elements.append(iv + ivx * x + ivy * y)
    return sorted(elements)

for _ in range(int(input())): print((lambda n, x, y, array: genMatrix(n, x, y, min(array)) == sorted(array) and 'YES' or 'NO')(*map(int, input().split(' ')), list(map(int, input().split(' ')))))