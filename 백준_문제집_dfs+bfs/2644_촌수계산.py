import sys
from collections import deque
N = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())
board = [[False]*(N+1) for _ in range(N+1)]
chk = [[False]*(N+1) for _ in range(N+1)]
for i in range(m):
    r, c = map(int, sys.stdin.readline().strip().split())
    board[r][c] = True
    board[c][r] = True
answer = -1
dq= deque()
dq.append((p1, 0))
while dq:
    p, cnt = dq.popleft()
    if p == p2:
        answer = cnt
        break
    for i in range(1, N+1):
        if board[p][i] == True and not chk[p][i]:
            dq.append((i, cnt+1))
            chk[p][i] = True

print(answer)
