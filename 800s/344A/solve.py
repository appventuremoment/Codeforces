curr, counter = "", 0
for _ in range(int(input())):
    magnet = input()
    if curr != magnet: curr, counter = magnet, counter + 1
print(counter)