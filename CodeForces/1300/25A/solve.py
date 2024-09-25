numbers = input()
lstofnum = list(map(int, input().split(' ')))

if [x % 2 for x in lstofnum[:3]].count(0) >= 2:
    lookfor = 1
else:
    lookfor = 0

for i in lstofnum:
    if i % 2 == lookfor:
        print(lstofnum.index(i) + 1)