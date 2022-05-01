import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    s = list(list(map(int, sys.stdin.readline().split())) for _ in range(2))
    dp=list([0]*(N+1) for _ in range(2))
    dp[0][1]=s[0][0]
    dp[1][1]=s[1][0]
    ans=max(s[1][0], s[0][0])
    for i in range(2, N+1):
        dp[0][i]=max(dp[1][i-1], max(dp[0][i-2], dp[1][i-2]))+s[0][i-1]
        dp[1][i]=max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2]))+s[1][i-1]
        ans=max(dp[0][i], dp[1][i])
    print(ans)

