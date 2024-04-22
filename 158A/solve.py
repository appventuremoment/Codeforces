leng, k = map(int, (input().split(' ')))
scores = list(map(int, input().split(' ')))
print([True for x in scores if x >= scores[k - 1] and x > 0].count(True))