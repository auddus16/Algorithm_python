import sys
N, M = map(int, sys.stdin.readline().strip().split())
parent = [i for i in range(N)]
def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

res = 0
for i in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    if find(x) == find(y):
        res = i+1
        break
    union(x, y)
print(res)