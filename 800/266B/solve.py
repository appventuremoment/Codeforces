length, times, queue = (*map(int, input().split(' ')), input())
for _ in range(times): queue = queue.replace('BG', 'GB')
print(queue)