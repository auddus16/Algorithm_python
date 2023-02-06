import sys
from collections import deque
N = int(sys.stdin.readline().strip())
board = [[0]*N for _ in range(N)]
bsx, bsy = 0, 0 # 아기상어 좌표
bs = 2 # 아기상어 크기 = 2
for i in range(N):
    a = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if a[j] == 9:
            bsx, bsy = i, j
            board[i][j] = 9
        elif 1 <= a[j] <= 6:
            board[i][j] = a[j]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def bfs(bsx, bsy):
    dq = deque()
    dq.append((bsx, bsy, 0))
    dist = []
    chk = [[False]*N for _ in range(N)]
    chk[bsx][bsy] = True
    while dq:
        x, y, n = dq.popleft()
        if 1 <= board[x][y] <= 6 and bs > board[x][y]: # 먹을 수 있는 물고기
           dist.append((n, x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not chk[nx][ny] and board[nx][ny] <= bs: # 지나갈 수 있는지
                dq.append((nx, ny, n+1))
                chk[nx][ny] = True

    dist.sort(key = lambda x : (x[0], x[1], x[2]))
    # print(dist)
    return dist

time = 0
cnt = 0 # 같은 크기 물고기 잡아먹는 경우 카운트
while True:
    fish = bfs(bsx, bsy)
    if len(fish) == 0:
        print(time)
        break

    board[bsx][bsy] = 0
    bsx, bsy = fish[0][1], fish[0][2]

    board[fish[0][1]][fish[0][2]] = 0
    time += fish[0][0]
    cnt += 1
    if cnt == bs:  # 크기 갱신
        bs += 1
        cnt = 0







