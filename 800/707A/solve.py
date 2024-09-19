output = '#Black&White'
for _ in range(int(input().split(' ')[0])):
    check = input().split(' ')
    if 'C' in check or 'M' in check or 'Y' in check: output = '#Color'
print(output)