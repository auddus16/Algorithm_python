import sys
from collections import deque
dx = (0, 1, 0, -1, 0, 0)
dy = (1, 0, -1, 0, 0, 0)
dr = (0, 0, 0, 0, 1, -1)

def bfs(sr, sx, sy):
    chk = [[[False] * C for _ in range(R)] for _ in range(L)]
    chk[sr][sx][sy] = True
    dq = deque()
    dq.append((sr, sx, sy, 0))

    while dq:
        r, x, y, res = dq.popleft()

        if b[r][x][y] == 'E':
            # print(res)
            return res

        for i in range(6):
            nr = r + dr[i]
            nx = x + dx[i]
            ny = y + dy[i]
            nres = res + 1
            # print(b[nr][nx][ny])
            if 0 <= nr < L and 0 <= nx < R and 0 <= ny < C:

                if b[nr][nx][ny] != '#' and not chk[nr][nx][ny]:
                    chk[nr][nx][ny] = True
                    dq.append((nr, nx, ny, nres))
    return 0

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break
    b = [[] for _ in range(L)]
    sx = 9
    sy = 7
    sr = 8
    for i in range(L):
        for j in range(R):
            b[i].append(list(sys.stdin.readline().strip()))
            if 'S' in b[i][j]:
                sr = i
                sx = j
                sy = b[i][-1].index('S')
        sys.stdin.readline()

    # print(b)
    # print(sr, sx, sy)
    ans = bfs(sr, sx, sy)
    if ans == 0:
        print('Trapped!')
    else:
        print(f'Escaped in {ans} minute(s).')
# print(b)
# print(sx, sy, sr)

