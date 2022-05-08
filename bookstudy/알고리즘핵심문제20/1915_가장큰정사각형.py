import sys
N, M= map(int, sys.stdin.readline().split())
arr=[list(map(int, input())) for _ in range(N)]
ans=max(arr[0])
for i in range(1, N):
    for j in range(1, M):
        if arr[i][j]==1:
            arr[i][j]=min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1]) +1
    ans=max(max(arr[i]), ans)
print(ans**2)