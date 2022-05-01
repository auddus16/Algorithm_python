import sys
from collections import deque
T = int(sys.stdin.readline())

dx = (-1, -1, -2, -2, +1, +1, +2, +2)
dy = (-2, +2, -1, +1, -2, +2, -1, +1)

for _ in range(T):
    I = int(sys.stdin.readline())

    chk = list([False] * I for _ in range(I))

    sr, sc = map(int, sys.stdin.readline().split())
    dr, dc = map(int, sys.stdin.readline().split())

    dq = deque()
    dq.append((sr, sc, 0))
    chk[sr][sc] = True

    while dq:
        r, c, cnt = dq.popleft()
        if r == dr and c == dc:
            print(cnt)
            break
        for i in range(8):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < I and 0 <= nc < I and not chk[nr][nc]:
                dq.append((nr, nc, cnt+1))
                chk[nr][nc] = True


