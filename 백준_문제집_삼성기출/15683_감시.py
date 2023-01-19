import copy
n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]: # cctv 번호, 위치
            cctv.append([data[j], i, j])

def fill(board, mm, x, y):
    for i in mm:  # 여러 모드
        nx = x
        ny = y
        while True: # 체크
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(ct, arr):
    global min_value

    if ct == len(cctv): # cctv 다 표시한 경우
        count = 0 # 감시영역 카운트
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count) # 최소값 갱신
        return
    temp = copy.deepcopy(arr) # 넘어온 그래프 상태 저장
    cctv_num, x, y = cctv[ct]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(ct+1, temp) # cctv개수 1증가, 변경된 그래프로 재귀호출
        temp = copy.deepcopy(arr) # 체크된 그래프 상태 되돌리기


min_value = int(1e9)
dfs(0, graph)
print(min_value)