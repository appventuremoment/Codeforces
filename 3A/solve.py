start = input()
end = input()

startcoord = (ord(start[0]) - 96, int(start[1]))
endcoord = (ord(end[0]) - 96, int(end[1]))
xdiff = endcoord[0] - startcoord[0]
ydiff = endcoord[1] - startcoord[1]


if xdiff > 0:
    xmove = 'R'
elif xdiff < 0:
    xmove = 'L'

if ydiff > 0:
    ymove = 'U'
elif ydiff < 0:
    ymove = 'D'

out = ''
count = 0
while xdiff != 0 or ydiff != 0:
    if xdiff == 0:
        movement = ''
    else:
        movement = xmove
        if xdiff > 0:
            xdiff -= 1
        else:
            xdiff += 1
    if ydiff != 0:
        movement += ymove
        if ydiff > 0:
            ydiff -= 1
        else:
            ydiff +=1
    
    count += 1
    out += '\n' + movement

print(str(count) + out)