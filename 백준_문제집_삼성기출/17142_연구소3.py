import sys
from itertools import combinations
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
virus = []
empty = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 2: # 바이러스
            virus.append((i, j))
        elif board[i][j] == 0: # 빈 칸
            empty += 1

if empty == 0: # 애초에 빈 칸 없음
    print(0)
    exit()

minV = int(1e9)

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

for i in list(combinations(virus, M)):
    dq = deque()
    chk = [[False] * N for _ in range(N)]
    for j in range(M):
        dq.append((i[j][0], i[j][1], 0)) # x, y, empty count
        chk[i[j][0]][i[j][1]] = True

    res = int(1e9)
    cnt = 0
    while dq:
        x, y, time = dq.popleft()
        if cnt == empty:
            break

        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0 <= nx <N and 0 <= ny < N and not chk[nx][ny]:
                if board[nx][ny] == 0: # 빈 칸인 경우
                    dq.append((nx, ny, time+1))
                    cnt += 1
                    chk[nx][ny] = True
                    if cnt == empty: # 빈 칸 다 놨을 경우 res 갱신
                        res = time + 1
                elif board[nx][ny] == 2: # 비활성 바이러스
                    dq.append((nx, ny, time+1))
                    chk[nx][ny] = True
    minV = min(res, minV)

if minV != int(1e9):
    print(minV)
else:
    print(-1)


