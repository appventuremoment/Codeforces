Mishka, Chris = 0, 0
for _ in range(int(input())):
    round = list(map(int, input().split(' ')))
    if round[0] > round[1]: Mishka += 1
    elif round[0] < round[1]: Chris += 1
if Mishka > Chris: print('Mishka')
elif Mishka < Chris: print('Chris')
else: print('Friendship is magic!^^')