input()
heights = list(map(int, input().split(' ')))
maxind = heights.index(max(heights))
minind = [i for i in range(len(heights))[::-1] if heights[i] == min(heights)][0]
if maxind > minind: print(maxind + (len(heights) - minind - 1) - 1)
else: print(maxind + (len(heights) - minind - 1))