maxi, curr = 0, 0
for _ in range(int(input())): curr, maxi = curr + (lambda x,y: y - x)(*map(int, input().split(' '))), max(maxi, curr)
print(maxi)