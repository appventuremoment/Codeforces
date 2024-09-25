############################################# Libraries ######################################################

import bisect
import sys
import math
import os
import time
from queue import PriorityQueue
from io import BytesIO, IOBase
from collections import defaultdict, Counter
from bisect import bisect_right

############################################# Definitions ######################################################

INF = sys.maxsize
BUFSIZE = 4096

############################################# Data Structures ######################################################

class SegmentTree:

    def init(arr): 
        n = len(arr)
        tree = [0]*(2*n)
        for i in range(n):
            tree[n+i] = arr[i]

        for i in range(n-1, -1, -1):
            tree[i] = tree[i << 1]+tree[(i << 1) | 1]
        return tree

    def add(tree, i, value):
        i += len(tree) // 2
        tree[i] = value
        while i > 1:
            tree[i >> 1] = tree[i] + tree[i ^ 1]
            i >>= 1
            
    def sum_index_range(tree, l, r):
        l += len(tree)//2
        r += len(tree)//2
        sum = 0
        while l < r:
            if l & 1:
                sum += tree[l]
                l += 1
            if r & 1:
                r -= 1
                sum += tree[r]
            l >>= 1
            r >>= 1
        return sum