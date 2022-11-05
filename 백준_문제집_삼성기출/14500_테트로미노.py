import sys
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
chk = [[False]*M for _ in range(N)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
maxV = 0

def dfs(x, y, s, cnt): # 행, 열, 합, 칸 개수
    global maxV

    if cnt == 4: # 모양 완성
        maxV = max(maxV, s)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and not chk[nx][ny]:
            chk[nx][ny] = True
            dfs(nx, ny, s+board[nx][ny], cnt+1)
            chk[nx][ny] = False

def exce(x, y):
    global maxV
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    case = [(0, 1, 2), (1, 2, 3), (2, 3, 0),(3, 0, 1)]
    for n in case:
        total = board[x][y]
        for i in range(3):
            nx = x + move[n[i]][0]
            ny = y + move[n[i]][1]
            if 0<=nx<N and 0<=ny<M:
                total += board[nx][ny]
            else:
                total = 0
                break

        maxV = max(total, maxV)

for i in range(N):
    for j in range(M):
        chk[i][j] = True
        dfs(i, j, board[i][j], 1)
        chk[i][j] = False

        exce(i, j)

print(maxV)

