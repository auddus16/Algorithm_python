import sys
N = int(sys.stdin.readline().strip())
a = [0]+list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * (N+1)

for i in range(1, N+1):
    maxV = 1
    for j in range(1, i):
        if a[j] < a[i]:
            maxV = max(maxV, dp[j]+1)
    dp[i] = maxV
# print(dp)
print(max(dp))