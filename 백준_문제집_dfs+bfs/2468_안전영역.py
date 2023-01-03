import sys
from collections import deque
N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
cnt = 0

dx = (0, 1, 0, -1)
dy = (1, 0, 1, 0)
rain = 0
maxV = max(map(max, board))
while rain <= maxV:
    ans = 0
    chk = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not chk[i][j] and board[i][j] > rain:
                dq = deque()
                dq.append((i, j))
                chk[i][j] = True
                ans += 1
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<N and 0<=ny<N and not chk[nx][ny] and board[nx][ny] > rain:
                            chk[nx][ny] = True
                            dq.append((nx, ny))
    cnt = max(cnt, ans)
    # print(cnt)
    rain += 1
print(cnt)


