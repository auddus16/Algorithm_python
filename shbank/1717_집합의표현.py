import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())

parent = [0] * (N+1) # 부모테이블 생성
for i in range(N+1):
    parent[i] = i # 자기자신을 부모로

def find(x):
    if x == parent[x]: # root node
        return x
    p = find(parent[x]) # x의 root 찾기
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
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')