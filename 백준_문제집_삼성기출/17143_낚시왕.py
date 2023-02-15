import sys
R, C, M = map(int, sys.stdin.readline().strip().split())
board = [[0]*C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().strip().split())
    board[r-1][c-1] = (s, d, z) # 속력, 방향, 크기

dx = (-1, +1, 0, 0) # 상하우좌
dy = (0, 0, +1, -1)

def move(r, c, s, d, z):
    cnt = 0
    if d == 1 or d == 2: # 상하
        while cnt < s:
            nr = r + dx[d-1]
            if nr < 0 or nr >= R: # 범위 넘었을 때
                d = 1 if d == 2 else 2
                r += dx[d-1]
            else:
                r = nr
            cnt += 1

        return (r, c, s, d, z)
    else: # 좌우
        while cnt < s:
            nc = c + dy[d-1]
            if nc < 0 or nc >= C:  # 범위 넘었을 때
                d = 3 if d == 4 else 4
                c += dy[d-1]
            else:
                c = nc
            cnt += 1

        return (r, c, s, d, z)

total = 0
for i in range(C):
    # i열에 있에서 땅에 가장 가까운 상어 잡기
    for x in range(R):
        if board[x][i] != 0:
            # print(board[x][i][2])
            total += board[x][i][2]
            board[x][i] = 0
            break
    # 상어 이동
    shark = []
    for x in range(R):
        for y in range(C):
            if board[x][y] != 0: # 상어
                shark.append(move(x, y, board[x][y][0], board[x][y][1], board[x][y][2]))
    # 상어 위치 갱신
    shark.sort()
    board = [[0]*C for _ in range(R)]
    bx, by = -1, -1
    for s in shark:
        if bx == -1 and by ==-1: # 맨처음 상어
            board[s[0]][s[1]] = (s[2], s[3], s[4])
            bx, by = s[0], s[1]
        else:
            if s[0] == bx and s[1] == by: # 같은 칸에 상어 2마리
                if s[4] > board[bx][by][2]: # 상어 갱신
                    board[bx][by] = (s[2], s[3], s[4])
            else:
                board[s[0]][s[1]] = (s[2], s[3], s[4])
                bx, by = s[0], s[1]
    # print(board)
print(total)
