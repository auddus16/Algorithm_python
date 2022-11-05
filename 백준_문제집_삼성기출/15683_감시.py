import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv.append((i, j))
d = ((1, 0), (-1, 0), (0, -1), (0, 1)) # 상하좌우
directions = [[(0), (1), (2), (3)], ((0, 1), (2, 3)), ((0, 3), (0, 2), (1, 2), (1, 3)), ((0, 1, 2), (1, 2, 3), (0, 2, 3), (0, 1, 3)), ((0, 1, 2, 3))]

# dq = deque()
# dq.append((cctv[0][0], cctv[0][1], 0)) # x, y, cnt
# while dq:
#     x, y, cnt = dq.popleft()
#     if board[x][y] == 1:
#         di = directions[0]
#         for i in di:
#             for j in i:
#                 dx = x+d[j]
#                 dy = y+d[j]

# for (x, y) in cctv:
#     maxV = 0
#     if board[x][y] == 1:
#         for i in directions[0]:
#             cnt = 0
#             for j in i:
#                 for k in range()



