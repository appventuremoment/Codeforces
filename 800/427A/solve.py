input()
hist = list(map(int, input().split(' ')))
counter = 0
police = 0
for x in hist:
    if x >= 0: police += x
    else:
        if police <= 0: counter += 1
        else: police -= 1
print(counter)