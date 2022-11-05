import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
virus, zero = [], []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
        else:
            continue

def bfs():
    global N, M
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    dq =deque()
    chk = [[False] * M for _ in range(N)]
    for v in virus:
        if not chk[v[0]][v[1]]:
            dq.append(v)
            chk[v[0]][v[1]] = True
            while dq:
                x, y = dq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<M and not chk[nx][ny] and board[nx][ny] != 1:
                        dq.append((nx, ny))
                        chk[nx][ny] = True
                        board[nx][ny] = 2
    # print(board)
# print(zero)
maxV = 0
for i in list(combinations(zero, 3)):
    tmp = deepcopy(board)
    # print(i)
    board[i[0][0]][i[0][1]] = 1
    board[i[1][0]][i[1][1]] = 1
    board[i[2][0]][i[2][1]] = 1
    # print(board)
    bfs()
    # print(board)
    total = 0
    for k in range(N):
        total += board[k].count(0)
    # print(total)
    maxV = max(maxV, total)
    board = tmp
print(maxV)


