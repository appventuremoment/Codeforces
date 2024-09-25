for _ in range(int(input())):
    b = input()
    print(''.join([b[x] for x in range(0, len(b), 2)]) + b[-1])