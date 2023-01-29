n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = [] # 사다리를 돌면서 가로선을 놓을 수 있는 후보군 저장
# 연속된 가로선은 놓을 수 없다는 조건이 있기 때문

for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check(): # 모든 열에 대해 i번째 열이 i번째에 도착할 수 있는지 확인
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(depth, idx): # 추가 개수 cnt, 가로선후보리스트 idx
    global answer

    if depth >= answer:
        return

    if check(): # 모든 열 도착 가능
        answer = depth
        return

    for c in range(idx, len(combi)): # 가로선 후보에서 하나씩 골라 재귀
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)
            visited[x][y] = False

for i in range(1,h+1): # 가로선 후보 저장 먼저 한다
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)