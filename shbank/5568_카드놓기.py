import sys
from itertools import permutations
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cl = [sys.stdin.readline().strip() for _ in range(n)]
res = []
for i in list(set(permutations(cl, k))):
    res.append(''.join(i))
print(len(set(res)))
