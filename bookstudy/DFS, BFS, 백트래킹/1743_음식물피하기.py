import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
board = list([False] * (1+M) for _ in range(N+1))
chk = list([False] * (1+M) for _ in range(N+1))
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    board[i][j] = True

cnt = 0
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def bfs(i, j):
    ans = 1
    dq = deque()
    dq.append((i, j))
    chk[i][j] = True
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 1 <= nr <= N and 1 <= nc <= M and not chk[nr][nc] and board[nr][nc]:
                chk[nr][nc] = True
                ans += 1
                dq.append((nr, nc))
    return ans

for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] and not chk[i][j]:
            cnt = max(cnt, bfs(i, j))

print(cnt)