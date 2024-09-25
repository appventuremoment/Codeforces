_, times = map(int, input().split(' '))
participants = list(map(int, input().split(' ')))

participantsdict = {}
for i in range(6): participantsdict[i] = participants.count(i)
print(sum([participantsdict[ind] for ind in range(6 - times)]) // 3)