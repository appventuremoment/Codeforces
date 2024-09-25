for _ in range(int(input())):
    n = int(input())
    if n % 4 != 0: print('NO')
    else:
        print('YES')
        outp = []
        for i in range(n // 4):
            outp.append(8 * i + 8)
            outp.append(8 * i + 12)
        for i in range(n // 4):
            outp.append(8 * i + 9)
            outp.append(8 * i + 11)
        assert sum(outp[len(outp) // 2:]) == sum(outp[:len(outp) // 2])
        print(" ".join(list(map(str, outp))))