from itertools import combinations
import sys
for i in combinations([int(sys.stdin.readline().strip()) for _ in range(9)], 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break