import sys
N, M, x, y, k = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dice = [0, 0, 0, 0, 0, 0]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

def turn(dir):
    d1, d2, d3, d4, d5, d6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if dir ==1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d4, d2, d1, d6, d5, d3
    elif dir == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d3, d2, d6, d1, d5, d4
    elif dir == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d5, d1, d3, d4, d6, d2
    else: # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d2, d6, d3, d4, d1, d5

a = list(map(int, sys.stdin.readline().strip().split()))
for i in range(k):
    nx, ny = x, y
    dir = a[i]
    nx += dx[dir-1]
    ny += dy[dir-1]

    if 0<= nx < N and 0<= ny < M:
        turn(dir)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0

        x, y = nx, ny
        print(dice[0])
