string = input()
longest = 0
for leng in range(1, len(string)):
    for x in range(len(string) - leng + 1):
        substr = string[x:x+leng]
        # print(substr)
        for y in range(x + 1, len(string) - leng + 1):
            if string[y:y+leng] == substr:
                longest = leng

print(longest)