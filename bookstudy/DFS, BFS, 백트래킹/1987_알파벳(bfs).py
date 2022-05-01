import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
board = list(list(sys.stdin.readline().strip()) for _ in range(R))
chk = [[set() for _ in range(C)] for _ in range(R)]
ans = 0
dq = deque()
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

chk.append(board[0][0])
dq.append((0, 0, board[0][0]))
while dq:
    r, c, a = dq.popleft()
    ans = max(ans, len(a))

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] not in a:
                na = a + board[nr][nc]
                if na not in chk[nr][nc]:
                    chk[nr][nc].add(na)
                    dq.append((nr, nc, na))
print(ans)