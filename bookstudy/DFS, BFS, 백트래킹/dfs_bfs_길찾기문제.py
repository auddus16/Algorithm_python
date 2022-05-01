from collections import deque

# 사방으로 움직이는 부분-상대좌표 저장. (왼, 위, 오, 아래)
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

# N * N 격자판 생성, 방문체크 할 배열 생성
N = int(input())
chk = [[False] * N for _ in range(N)]

# (x, y)가 가능한 범위인지 확인하는 메소드
def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

# dfs
def dfs(y, x):
    if adj[y][x] == ans:
        return
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            chk[ny][nx] = True
            dfs(ny, nx)

# bfs
def bfs(sy, sx):
    q = deque()
    chk[sy][sx] = True
    q.append((sy, sx))

    while len(q):
        y, x = q.popleft()
        if adj[y][x] == ans:
            return

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append(ny, nx)