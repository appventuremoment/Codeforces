def genString(length, array):
    counter, string = dict(zip(list("abcdefghijklmnopqrstuvwxyz"), [0 for _ in range(26)])), ""
    for item in array:
        ind = list(counter.keys())[list(counter.values()).index(item)]
        string += ind
        counter[ind] += 1
    print(string)


for _ in range(int(input())): genString(int(input()), list(map(int, input().split(' '))))