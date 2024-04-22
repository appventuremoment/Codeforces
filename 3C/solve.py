board = []
for i in range(3):
    board.append(input())

def checkwin(positions):
    winno, won = 0, False
    if (1, 1) in positions:
        if (0, 0) in positions and (2, 2) in positions:
            won = True
            winno += 1
        if (0, 2) in positions and (2, 0) in positions:
            won = True
            winno += 1
    
    rows = [x[0] for x in positions]
    cols = [x[1] for x in positions]

    for i in range(3):
        if rows.count(i) == 3:
            won = True
            winno += 1
        if cols.count(i) == 3:
            won = True
            winno += 1

    return won, winno

def TTTeval(board):
    xpos, opos = [], []
    for row, line in enumerate(board):
        for col, char in enumerate(line):
            if char == 'X':
                xpos.append((row, col))
            if char == '0':
                opos.append((row, col))

    xwon, xwinno = checkwin(xpos)
    owon, owinno = checkwin(opos)

    if xwon and owon:
        return 'illegal'
    if xwinno + owinno > 2:
        return 'illegal'    
    if len(opos) - len(xpos) > 0 or len(xpos) - len(opos) > 1:
        return 'illegal'
    
    if xwon:
        if len(xpos) - len(opos) == 1:
            return 'the first player won'
        else:
            return 'illegal'
    if owon:
        if len(xpos) - len(opos) == 0:
            return 'the second player won'
        else:
            return 'illegal'


    if len(xpos) + len(opos) == 9:
        return 'draw'
    elif len(xpos) == len(opos):
        return 'first'
    elif len(xpos) > len(opos):
        return 'second'


print(TTTeval(board))