import re
leng = int(input())
for x in range(leng):
    inp = input()
    if re.match('R[\d]+C[\d]+', inp):
        ROW = inp.split('C')[0][1:]
        inpCOLUMN = int(inp.split('C')[1])
        temp = []
        while inpCOLUMN != 0:
            if inpCOLUMN % 26 == 0:
                inpCOLUMN = inpCOLUMN // 26 - 1
                temp.append(26)
            else:
                temp.append(inpCOLUMN % 26)
                inpCOLUMN //= 26
        temp = [x for x in temp if x != 0]
        temp = temp[::-1]
        count = 0
        COLUMN = ''
        for inp in temp:
            COLUMN += chr(64 + inp)
        print(f"{COLUMN}{ROW}")
    else:
        ROW = ''.join([x if x.isnumeric() else '' for x in inp])
        COLUMNinp = ''.join([x if x.isalpha() else '' for x in inp][::-1])
        COLUMN = 0
        count = 0
        for x in COLUMNinp:
            COLUMN += (ord(x) - 64) * 26 ** count
            count += 1
        print(f"R{ROW}C{COLUMN}")
