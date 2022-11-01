import sys
n, k = map(int, sys.stdin.readline().strip().split())
coin = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0]*(k+1)
# coin.sort()
for i in range(1, k + 1):
    a = []
    for j in coin:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
# print(dp)
print(dp[k])
