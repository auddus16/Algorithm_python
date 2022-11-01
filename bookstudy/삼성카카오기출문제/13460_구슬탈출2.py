import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

srx, sry, sbx, sby = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            sbx, sby = i, j
        elif board[i][j] == 'R':
            srx, sry = i, j
# print('시작위치')
# print(srx, sry, sbx, sby)
def go_next(rx, ry, bx, by, k):
    nrx, nry, nbx, nby = rx, ry, bx, by

    while True: # Red
        nrx = nrx + dx[k]
        nry = nry + dy[k]

        if nrx < N and nry < M:
            if board[nrx][nry] == '#':
                nrx = nrx - dx[k]
                nry = nry - dy[k]
                break
            elif board[nrx][nry] == 'O': # 입구 찾아서 나간 경우
                nrx, nry = -1, -1
                break
        else:
            nrx = nrx - dx[k]
            nry = nry - dy[k]
            break


    while True:# Blue
        nbx = nbx + dx[k]
        nby = nby + dy[k]

        if nbx < N and nby < M:
            if board[nbx][nby] == '#':
                nbx = nbx - dx[k]
                nby = nby - dy[k]
                break
            elif board[nbx][nby] == 'O': # 입구 찾아서 나간 경우
                nbx, nby = -1, -1
                break
        else:
            nbx = nbx - dx[k]
            nby = nby - dy[k]
            break

    if nrx == -1 and nbx == -1: # 둘 다 빠져버리는 경우
        # print('둘다빠짐')
        return False

    # 구슬들이 구멍에 빠지지 않았으면서 충돌했을 경우 (나란히 위치시켜준다..)
    if nrx != -1 and nbx != -1 and (nrx == nbx and nry == nby):
        if k == 0: # right(0, 1)
            if ry < by:
                nry -= 1
            else:
                nby -= 1
        elif k == 1: # left(0, -1)
            if ry < by:
                nby += 1
            else:
                nry += 1
        elif k == 2: # down(1, 0)
            if rx < bx:
                nrx -= 1
            else:
                nbx -= 1
        else: # up(0, -1)
            if rx < bx:
                nbx += 1
            else:
                nrx += 1

    return nrx, nry, nbx, nby


def bfs():
    # print()
    dq = deque()
    chk = set()
    chk.add((srx, sry, sbx, sby))
    dq.append((srx, sry, sbx, sby, 0))

    while dq:
        rx, ry, bx, by, cnt = dq.popleft()
        if bx == -1 and by == -1: # 파란구슬이 구멍에 빠지면 실패
            continue
        if rx == -1 and ry == -1:
            return cnt

        if cnt < 10:
            ncnt = cnt + 1
            for k in range(4):
                if go_next(rx, ry, bx, by, k):
                    nrx, nry, nbx, nby = go_next(rx, ry, bx, by, k)
                    if (nrx, nry, nbx, nby) not in chk:
                        chk.add((nrx, nry, nbx, nby))
                        dq.append((nrx, nry, nbx, nby, ncnt))
                # print(dq)
    return -1

print(bfs())

