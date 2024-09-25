borze = input()

ind = 0
out = ""
while ind < len(borze):
    if borze[ind] == ".": out += '0'; ind += 1
    elif borze[ind] + borze[ind + 1] == "-.": out += '1'; ind += 2
    else: out += '2'; ind += 2
print(out)