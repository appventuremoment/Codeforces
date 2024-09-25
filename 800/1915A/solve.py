for _ in range(int(input())):
    temp = list(map(int, input().split(' ')))
    if temp[0] == temp[1]: print(temp.pop())
    elif temp.pop() == temp[0]: print(temp[1])
    else: print(temp[0])