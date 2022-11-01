import sys
N = int(sys.stdin.readline().strip())
a = [int(sys.stdin.readline().strip()) for _ in range(N)]
dp = [0]*(N+1)

a.sort()
for i in range(1, N+1):
    dp[i] = a[N-i]*i
# print(dp)
print(max(dp))