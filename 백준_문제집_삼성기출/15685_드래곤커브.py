import sys
N = int(sys.stdin.readline().strip())
arr = [[False]* 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().strip().split())
    arr[x][y] = True

    move = [d]

    # g세대 만들기
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1]+1) % 4)
        move.extend(tmp)

    # 드래곤 커브 좌표 표시하기
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = True
        x = nx
        y = ny

# 모든 좌표에 대해 정사각형 개수 구하기
res = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            res += 1
print(res)