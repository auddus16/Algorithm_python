import sys
N = int(sys.stdin.readline().strip())
std = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N**2)]
board = [[0]*N for _ in range(N)]

# 학생 앉히기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in std:
    s = i[0] # s번 학생 자리
    tmp = [] # 가능한 자리 다 담은 후, 정렬
    for j in range(N):
        for k in range(N):
            if board[j][k]==0: # 빈 자리
                like = 0
                blank = 0
                for l in range(4):
                    nr = j + dr[l]
                    nc = k + dc[l]
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] in i[1:]:
                            like += 1
                        if board[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, j, k])
    # tmp정렬해서 가장 앞에 있는 자리에 학생 앉히기
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    board[tmp[0][2]][tmp[0][3]] = s
# print(board)
# 학생 만족도 계산
res = 0
std.sort() # 학생 순서가 정렬되어야 idx로 접근 가능 (학생번호-1) = index
for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] in std[board[i][j]-1][1:]:
                    ans += 1
        if ans != 0:
            res += 10 ** (ans-1)
print(res)


