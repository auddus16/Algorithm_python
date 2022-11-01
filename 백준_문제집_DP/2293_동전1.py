import sys
n, k = map(int, sys.stdin.readline().strip().split())
coin = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1
for c in coin:
    for i in range(1, k+1):
        if i>=c:
            dp[i] += dp[i-c]
print(dp[k])