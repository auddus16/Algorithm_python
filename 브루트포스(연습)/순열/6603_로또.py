import sys
from itertools import combinations

input= sys.stdin.readline

while True:
    a= list(map(int, input().split()))
    if a[0]==0:
        break
    del a[0]

    res= list(combinations(a, 6))
    for i in res:
        for j in i:
            print(j, end=' ')
        print()
    print()