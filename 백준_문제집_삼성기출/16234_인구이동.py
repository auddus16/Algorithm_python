import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().strip().split())
nations = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# print(nations)

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
def bfs(r, c): # 연합국
    dq = deque()
    dq.append((r, c))
    chk[r][c] = True

    union = [(r, c)]
    count = nations[r][c] # union total

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<= ny <N and not chk[nx][ny]:
                if L<= abs(nations[nx][ny]-nations[x][y]) <=R:
                    union.append((nx, ny))
                    count += nations[nx][ny]
                    dq.append((nx, ny))
                    chk[nx][ny] = True

    # 인구 수 갱신
    for x, y in union:
        nations[x][y] = count // len(union)

    # 연합국 면적 리턴
    return len(union)


cnt = 0 # 일 수
while True: # 인구 이동이 없을 때까지 반복한다.
    flag = False
    chk = [[False]*N for _ in range(N)]

    # 모든 좌표를 bfs로 방문하여 연합 진행
    for i in range(N):
        for j in range(N):
            if not chk[i][j]:
                if bfs(i, j) > 1: # 연합국 면적이 2이상일 경우, 인구 이동 有
                    flag = True

    # 인구 이동이 없는 경우
    if not flag:
        break

    # 일 수 + 1
    cnt += 1

print(cnt)


