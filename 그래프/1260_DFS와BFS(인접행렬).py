import sys
from collections import deque
N, M, V=map(int, sys.stdin.readline().split())
input=[list(map(int, sys.stdin.readline().split())) for _ in range(M)]

E=[[0]*(N+1) for i in range(N+1)]#인접행렬
for i in input:
    E[i[0]][i[1]]=1
    E[i[1]][i[0]]=1

def dfs(x, check):
    check[x]=True
    print(x,end=' ')
    for i in range(1, N+1):
        if E[x][i]==1 and check[i]==False:
            dfs(i, check)

def bfs(s, check):
    q=deque([s])
    check[s]=True
    while q:
        x=q.popleft()
        print(x,end=' ')
        for i in range(1, N+1):
            if E[x][i]==1 and check[i]==False:
                q.append(i)
                check[i]=True

dfs(V, [False]*(N+1))
print()
bfs(V, [False]*(N+1))
