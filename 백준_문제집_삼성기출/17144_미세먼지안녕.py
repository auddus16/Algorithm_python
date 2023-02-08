import sys
R, C, T = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
up, down = -1, -1
for i in range(R): # 공기청정기 위치 저장
    if board[i][0] == -1:
        up = i
        down = i+1
        break

def step1(): # 미세먼지 확산
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    tmp_arr = [[0] * C for _ in range(R)] # 추가될 미세먼지 양 저장
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1:
                tmp = 0 # 감소되는 미세먼지 양
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        tmp_arr[nx][ny] += board[i][j] // 5 # 추가될 양
                        tmp += board[i][j] // 5
                board[i][j] -= tmp
                # 현재 칸에서 줄어드는 양은 이후 확산에 영향을 미치지 않는다.
                # 줄어드는 양은 바로 갱신 가능
                # 다른 칸으로부터 추가되는 양은 이후 확산을 시작할 떄 영향을 주므로,
                # tmp_arr에 추가 양을 저장 후, 일괄 갱신해준다.

    for i in range(R):
        for j in range(C):
            board[i][j] += tmp_arr[i][j]

def step2(up, down):
    # 위쪽으로 이동
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C: # 범위 넘어가면 다음 방향으로 전환
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny

    # 아래쪽 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C: # 범위 넘어가면 다음 방향으로 전환
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny

for _ in range(T):
    step1()
    step2(up, down)
res = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            res += board[i][j]

print(res)

