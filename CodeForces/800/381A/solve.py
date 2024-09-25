import collections

input()
deck = collections.deque(list(map(int, input().split(' '))))
first, second = [], []
for x in range(len(deck)):
    ind = deck.index(max(deck[0], deck[-1]))
    if ind > 0: add = deck.pop()
    else: add = deck.popleft()
    if x % 2 == 0: first.append(add)
    else: second.append(add)
print(sum(first), sum(second))