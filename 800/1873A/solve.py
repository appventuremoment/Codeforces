for _ in range(int(input())):
    temp = input()
    if 'a' == temp[2] and 'c' == temp[0]: print('YES')
    elif 'a' == temp[2] or 'c' == temp[0]: print('NO')
    else: print('YES')