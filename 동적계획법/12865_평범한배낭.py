import sys
N, K= map(int, sys.stdin.readline().split())
a= list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
dp=[[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w=a[i-1][0]
        v=a[i-1][1]
        if j < w:
            dp[i][j]= dp[i-1][j]
        else:
            dp[i][j]= max(dp[i-1][j-w]+v, dp[i-1][j])
print(dp[-1][-1])

