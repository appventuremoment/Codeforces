print((lambda length, stones: [stones[x] == stones[x + 1] for x in range(length - 1)].count(True))(int(input()), list(input())))