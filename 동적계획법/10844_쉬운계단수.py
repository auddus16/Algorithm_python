import sys
N=int(sys.stdin.readline())
dp=list([0]*10 for _ in range(N+1))
for i in range(1, 10):
    dp[1][i]=1
for i in range(2, N+1):
    for j in range(10):
        if j-1>=0: # -1가능
            dp[i][j]+=dp[i-1][j-1]
        if j+1<=9: # +1 가능
            dp[i][j]+=dp[i-1][j+1]
        dp[i][j]%=1000000000
print(sum(dp[N])%1000000000)