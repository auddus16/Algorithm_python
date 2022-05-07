import sys
from collections import deque
N, M= map(int, sys.stdin.readline().split())
arr=[[False]*N for _ in range(N)]
for i in range(M):
    a, b= map(int, sys.stdin.readline().split())
    arr[a-1][b-1]=True
    arr[b-1][a-1]=True

ans = -1
ans_tot=987654321
total=[[0]*N for _ in range(N)]

def bfs(s, e):
    chk=[False]*N
    dq=deque()
    chk[s]=True
    dq.append((s, 0))
    while dq:
        now, d= dq.popleft()
        if now == e:
            return d
        for k in range(N):
            if arr[now][k] and not chk[k]: # now->k 길이 존재, 아직 k를 방문하지 않았다면,
                chk[k]=True
                dq.append((k, d+1))

for i in range(N):
    tot=0
    for j in range(N):
        if i!=j:
            if total[i][j]==0: # 아직 구해지지 않은 경우
                total[i][j]=total[j][i]=bfs(i, j)

            tot+=total[i][j]
    if ans_tot > tot:
        ans= i
        ans_tot = tot
print(ans+1)