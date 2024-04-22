for _ in range(int(input())):
    leng = int(input())
    arr = sorted(list(map(int, input().split(' '))))
    print(len([x for x in arr[leng // 2 + leng % 2 - 1:] if x == arr[leng // 2 + leng % 2 - 1]]))