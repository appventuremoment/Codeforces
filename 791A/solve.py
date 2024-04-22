import math 
print((lambda a, b: (math.log(b) - math.log(a)) == math.log(1.5) and 2 or a != b and math.ceil((math.log(b) - math.log(a)) / math.log(1.5)) or 1)(*map(int, input().split(' '))))

# 3 ** n  * a - 2 ** n * b > 0
# (3 / 2) ** n > b / a
# n > (log b - log a) / log 1.5

# Exception cases are when (log b - log a) / log 1.5 is 1 or a == b