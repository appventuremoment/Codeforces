leng = int(input())

timeline = []
finalscores = {}
for i in range(leng):
    temp = input().split(' ')
    if temp[0] in finalscores.keys():
        finalscores[temp[0]] += int(temp[1])
    else:
        finalscores[temp[0]] = int(temp[1])
    timeline.append((temp[0], int(temp[1])))

finalists = [x for x in finalscores if finalscores[x] == max(finalscores.values())]
finaliststimeline = [x for x in timeline if x[0] in finalists]
maxscore = max(finalscores.values())

scoreboard = dict(zip(finalists, [0] * len(finalists)))

for i in finaliststimeline:
    scoreboard[i[0]] += i[1]
    if scoreboard[i[0]] >= maxscore:
        print(i[0])
        break