import sys
N=int(sys.stdin.readline())
a=list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
dp=list([0]*(N) for _ in range(N))
dp[0][0]=a[0][0]
for i in range(1, N):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+a[i][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-1])+a[i][j]
print(max(dp[N-1]))
