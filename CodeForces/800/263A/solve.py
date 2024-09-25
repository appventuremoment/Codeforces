for y in range(5): 
    out = (lambda line: abs(y - 2) + abs(line.index(1) - 2) if 1 in line else -1)(list(map(int, input().split(' '))))
    if out != -1: print(out)