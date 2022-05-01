import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
adj = [[False] * (N+1) for _ in range(N+1)]
chk = [False] * (N+1)
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s][e] = True
    adj[e][s] = True
cnt = 0
def dfs(s):
    for i in range(1, N+1):
        if adj[s][i] and not chk[i]:
            chk[i] = True
            dfs(i)
for i in range(1, N+1):
    if not chk[i]:
        cnt += 1
        chk[i] = True
        dfs(i)
print(cnt)