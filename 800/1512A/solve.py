for _ in range(int(input())):
    input()
    amongus = list(map(int, input().split(' ')))
    hash = {item: amongus.count(item) for item in amongus}
    print(amongus.index(list(hash.keys())[list(hash.values()).index(1)]) + 1)