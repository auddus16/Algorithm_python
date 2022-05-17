import sys
from itertools import permutations
N=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
max_V=-99999999
for i in permutations(a):
    tot=0
    for j in range(N-1):
        tot+=abs(i[j]-i[j+1])
    max_V=max(max_V, tot)
print(max_V)