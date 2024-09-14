home, guest = [], []
for _ in range(int(input())):
    temp, temp2 = map(int, input().split(' '))
    home.append(temp)
    guest.append(temp2)

counter = 0
for i in range(len(home)):
    counter += len([x for x in guest[:i] + guest[i+1:] if x == home[i]])
print(counter)