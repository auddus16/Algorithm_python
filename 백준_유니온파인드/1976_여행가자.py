import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
parent = [i for i in range(N)]
def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# 유니온
for i in range(N):
    link = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if link[j] == 1:
            union(i, j)

#파인드
path = list(map(int, sys.stdin.readline().strip().split()))
start = parent[path[0]-1] # 여행 경로 첫 번째 지점의 부모에서 시작
for i in range(1, M):
    if parent[path[i]-1] != start:
        print('NO')
        break
else:
    print('YES')

