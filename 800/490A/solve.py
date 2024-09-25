input()
children = list(map(int, input().split(' ')))
one, two, three = [x + 1 for x in range(len(children)) if children[x] == 1], [x + 1 for x in range(len(children)) if children[x] == 2], [x + 1 for x in range(len(children)) if children[x] == 3]
teams = min([len(one), len(two), len(three)])
print(teams)
for i in range(teams): print(one[i], two[i], three[i])