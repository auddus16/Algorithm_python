import sys
from collections import deque
N = int(sys.stdin.readline().strip())
board = [[0]*N for _ in range(N)]
K = int(sys.stdin.readline().strip())
for _ in range(K):
    i, j = map(int, sys.stdin.readline().strip().split())
    board[i-1][j-1] = 2
L = int(sys.stdin.readline().strip())
move = {}
for _ in range(L):
    a = list(sys.stdin.readline().strip().split())
    move[int(a[0])] = a[1]
# print(move)

# 상 우 하 좌
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

time = 0
dq = deque()
i, j = 0, 0
dq.append((i, j))
board[0][0] = 1
direction = 0
while True:
    time += 1
    global direation
    i += dx[direction]
    j += dy[direction]

    if i<0 or i>=N or j<0 or j>=N or board[i][j] == 1:
        # print(i, j)
        break

    # 전진
    if board[i][j] == 0: # apple X -> 꼬리 제거
        tmp_x, tmp_y = dq.popleft()
        board[tmp_x][tmp_y] = 0

    dq.append((i, j))
    board[i][j] = 1

    if time in move.keys():
        if move[time] == 'D': # right
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

    # print(time)

# print(dq)
print(time)


