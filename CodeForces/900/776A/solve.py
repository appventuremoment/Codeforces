namelist = input().split(' ')
print(" ".join(namelist))
for _ in range(int(input())):
    killed, replacement = input().split(' ')
    namelist[namelist.index(killed)] = replacement
    print(" ".join(namelist))