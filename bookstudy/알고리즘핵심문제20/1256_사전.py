import sys
N, M, K = map(int, sys.stdin.readline().split())
dp = list([0]*(M+1) for _ in range(N+1))
for j in range(1, M+1):
    dp[0][j]=1
for i in range(1, N+1):
    dp[i][0]=1
    for j in range(1, M+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
ans=''
def s(n, m, k):
    global ans
    if n==0:
        ans=ans+('z'*m)
        return
    elif m==0:
        ans=ans+('a'*n)
        return
    if dp[n-1][m]>=k: #앞에 a
        ans=ans+'a'
        s(n-1, m, k)
    else: #앞에 z
        ans=ans+'z'
        s(n, m-1, k-dp[n-1][m])

if K>dp[N][M]:
    print(-1)
else:
    s(N, M, K)
    print(ans)

