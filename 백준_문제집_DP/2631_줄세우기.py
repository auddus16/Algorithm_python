import sys
N = int(sys.stdin.readline().strip())
num = [int(sys.stdin.readline().strip()) for _ in range(N)]
num.insert(0, 1)
dp = [1] * (N+1)

for i in range(1, N+1):
    for j in range(1, i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))