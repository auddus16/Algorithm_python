import sys
from collections import deque
N = int(sys.stdin.readline().strip())
board = [sys.stdin.readline().strip() for _ in range(N)]
chk = [[False]*N for _ in range(N)]
res = []
# print(board)
def bfs(r, c):
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    dq = deque()
    dq.append((r, c))
    chk[r][c] = True

    cnt = 1
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not chk[nx][ny] and board[nx][ny] == '1':
                cnt += 1
                chk[nx][ny] = True
                dq.append((nx, ny))
    return cnt

for i in range(N):
    for j in range(N):
        if not chk[i][j] and board[i][j]=='1':
            res.append(bfs(i, j))
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])


