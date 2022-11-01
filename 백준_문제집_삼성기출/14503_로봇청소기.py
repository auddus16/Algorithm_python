import sys
N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dx = (-1, 0, 1, 0) # 북 동 남 서
dy = (0, 1, 0, -1)

cnt = 1
board[r][c] = 2
while True:
    # print(r, c)
    flag = False
    # 현재방향 d를 기준으로 왼쪽 방향으로 탐색
    for _ in range(4):
        nr = r + dx[(d+3)%4]
        nc = c + dy[(d+3)%4]
        d = (d + 3) % 4 # 탐색하는 순간 방향 갱신해주기
        if board[nr][nc] == 0: # 청소 가능
            r = nr
            c = nc
            cnt += 1
            board[r][c] = 2
            flag = True
            break
    if not flag: # 4방향 모두 갈 수 없는 경우
        # print(back)
        if board[r-dx[d]][c-dy[d]] != 1: # 후진
            r = r-dx[d]
            c = c-dy[d]
        else:
            print(cnt)
            # print(board)
            break


