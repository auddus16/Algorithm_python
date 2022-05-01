import sys
from itertools import combinations
N, M= map(int, sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
max=0
for i in combinations(num, 3):
    if max<sum(i)<=M:
        max=sum(i)
print(max)