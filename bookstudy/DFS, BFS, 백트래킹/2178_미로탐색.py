import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
chk = [[False] * M for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

dq = deque()
dq.append((0, 0, 1)) # y, x, cnt, 첫번째 노드에서 출발
chk[0][0] = True

def is_valid_coord(y, x):
    return 0 <= y < N and 0<= x < M

while len(dq) > 0:
    y, x, d = dq.popleft()

    if y == N-1 and x == M-1: # 마지막 노드에 도착
        print(d)
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        nd = d + 1
        if is_valid_coord(ny, nx) and not chk[ny][nx] and board[ny][nx] == '1':
            chk[ny][nx] = True
            dq.append((ny, nx, nd))

