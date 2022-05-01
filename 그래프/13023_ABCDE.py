import sys
N, M= map(int, sys.stdin.readline().split())
rel=[list(map(int, sys.stdin.readline().split())) for _ in range(M)]
E=[[] for _ in range(N)]
for i in rel:
    E[i[0]].append(i[1])
    E[i[1]].append(i[0])
check=[False]*N

def dfs(idx, cnt):
    if cnt==4:
        print(1)
        exit()
    for i in E[idx]:
        if not check[i]:
            check[i]=True
            dfs(i, cnt+1)
            check[i]=False

for i in range(N):
    check[i]=True
    dfs(i, 0)
    check[i]=False

print(0)