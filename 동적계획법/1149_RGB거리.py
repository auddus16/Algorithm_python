import sys
N=int(sys.stdin.readline())
a=list(list(map(int,sys.stdin.readline().split())) for _ in range(N))
dp=list([0, 0, 0] for _ in range(N+1))
for i in range(1, N+1):
    dp[i][0]=min(dp[i-1][1], dp[i-1][2])+a[i-1][0]
    dp[i][1]=min(dp[i-1][0], dp[i-1][2])+a[i-1][1]
    dp[i][2]=min(dp[i-1][0], dp[i-1][1])+a[i-1][2]
print(min(dp[N][0], dp[N][1], dp[N][2]))