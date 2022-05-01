import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    dp = [1, 1, 1, 2, 2]
    for i in range(5, N):
        dp.append(dp[i-1]+dp[i-5])
    print(dp[N-1])