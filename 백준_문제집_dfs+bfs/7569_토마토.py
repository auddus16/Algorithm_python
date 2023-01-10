import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().strip().split())
board = []
chk = [[[False]*M for _ in range(N)] for _ in range(H)]
for _ in range(H):
    board.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
# print(board)
dq = deque() # 익은 토마토
t2 = 0 # 안 익은 토마토
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1: # 큐에 먼저 처음 토마토 위치를 담아야 함 -> 토마토가 서로 인접하지 않을 경우 존재하기 때문
                dq.append((0, (i, j, k)))
            elif board[i][j][k] == 0:
                t2 += 1
if t2 == 0: # 저장될 때부터 모든 토마토가 익은 상태
    print(0)
else:
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    df = (1, -1)
    maxV = 0
    while dq:
        day, p = dq.popleft()
        for i in range(4):
            nx = p[1]+dx[i]
            ny = p[2]+dy[i]
            if 0<=nx<N and 0<=ny<M and board[p[0]][nx][ny] == 0:
                dq.append((day+1, (p[0], nx, ny)))
                maxV = max(day+1, maxV)
                board[p[0]][nx][ny] = 1
                t2 -= 1 # 안 익은 토마토 -1
        for i in range(2):
            nf = p[0]+df[i]
            if 0<=nf<H and board[nf][p[1]][p[2]] == 0:
                dq.append((day+1, (nf, p[1], p[2])))
                maxV = max(day+1, maxV)
                board[nf][p[1]][p[2]] = 1
                t2 -= 1  # 안 익은 토마토 -1
    if t2 == 0:
        print(maxV)
    elif t2 > 0:
        print(-1)




