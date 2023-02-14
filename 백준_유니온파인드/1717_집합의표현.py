import sys
N, M = map(int, sys.stdin.readline().strip().split())
sys.setrecursionlimit(10**6)
parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i # 자기자신을 부모로

def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(M):
    op, a, b = map(int, sys.stdin.readline().strip().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')