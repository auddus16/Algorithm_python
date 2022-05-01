import sys
from collections import deque

N, M, V= map(int, sys.stdin.readline().split())
input=[list(map(int, sys.stdin.readline().split())) for _ in range(M)]

E= [[] for _ in range(N+1)]
for i in input: #인접리스트
    E[i[0]].append(i[1])
    E[i[1]].append(i[0])

for i in range(1, N+1):
    E[i].sort()

def dfs(x, check):
    print(x,end=' ')
    check[x]=True
    for i in range(0, len(E[x])):
        y=E[x][i]
        if not check[y]:
            dfs(y, check)

def bfs(s, check):
    q=deque([s])
    check[s]=True
    while q:
        x=q.popleft()
        print(x,end=' ')
        for i in range(0, len(E[x])):
            y=E[x][i]
            if not check[y]:
                check[y]=True
                q.append(y)

dfs(V, [False]*(N+1))
print()
bfs(V, [False]*(N+1))