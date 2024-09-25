index = []
diff = []
leng = int(input()) - 1
for i in range(leng):
    a, b = list(map(int, input().split(' ')))
    index.append([a, b])
    diff.append(abs(b - a))

maxi = 0
for x in range(leng):
    for y in range(x + 1, leng):
        if diff[x] * diff[y] > maxi:
            #this part has issues
            a1, b1 = index[x][0], index[x][1]
            a2, b2 = index[y][0], index[y][1]
            
            # maxi = diff[x] * diff[y]


print(index, diff)